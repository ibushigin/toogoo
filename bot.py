import discord
from discord.ext import commands
from tgtg import TgtgClient
import json
from pathlib import Path
import env


#I need token.json to complete the API request and get the list of items available
def getItems():
    pathToFile = 'token.json'
    path = Path(pathToFile)
    #I check if token.json exists
    if path.is_file():
        print("Token found")
    #if not exist, i sent a request with my email to get tokens
    else:    
        client = TgtgClient(env.email)
        credentials = client.get_credentials()
        print(credentials)
        with open("token.json", "w") as outfile:
            json.dump(credentials, outfile)
        print("Json created")

    #import token and get raw items list
    f2 = open('token.json')
    tokens = json.load(f2)
    client = TgtgClient(
        access_token=tokens['access_token'],
        refresh_token=tokens['refresh_token'],
        user_id=tokens['user_id']
        )
    items = client.get_items()
    f2.close()
    print("got items")
    return items

#check if basket is available
def ItemsAvailable():
    items = getItems()
    for i in items:        
        if 0 == i["items_available"]:            
            return False
        else:
            list = []
            for i in items:
                if i["items_available"] != 0:
                    value = i["item"]["value_including_taxes"]["minor_units"]/100
                    price = i["item"]["price_including_taxes"]["minor_units"]/100
                    item = {
                        "shop" : i["store"]["store_name"],
                        "number of item" : str(i["items_available"]),
                        "value" : str(value)+"€",
                        "price" : str(price)+"€"
                    }
                    list.append(item)    
        return list

##### DISCORD BOT
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    canal = bot.get_channel(env.canal)
    await canal.send("`Rachel est éveillée`")

@bot.command("panier")
async def panier(ctx): 
    '''Envoie la liste des paniers
    '''
    canal = bot.get_channel(env.canal)
    items = ItemsAvailable()
    if False == items:
        await canal.send("`Il n'y a pas de panier disponible!`")
    else:
        for i in items:
            store = i["shop"]   
            num = i["number of item"] 
            value = i["value"]
            price = i["price"]    
            await canal.send("`"+num+" panier(s) disponible chez "+store+" à "+price+" ("+value+")!`")

@bot.command("replicant?")
async def replicant(ctx): 
    '''You come across a full page of nude photos of a girl.
    '''
    canal = bot.get_channel(env.canal)
    author = str(ctx.message.author.name)
    await canal.send("`Is this testing whether I'm a Replicant or a lesbian, Mr "+author+"?`")


bot.run(env.botToken)