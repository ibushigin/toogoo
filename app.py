from tgtg import TgtgClient
import json
from pathlib import Path

#Create token
pathToFile = 'token.json'
path = Path(pathToFile)
if path.is_file():
    print("Token found")
else:    
    client = TgtgClient(email="jexn.lxlxnne@gmail.com")
    credentials = client.get_credentials()
    print(credentials)
    with open("token.json", "w") as outfile:
        json.dump(credentials, outfile)
    print("Json created")

#import token and get items
f2 = open('token.json')
tokens = json.load(f2)
client = TgtgClient(
    access_token=tokens['access_token'],
    refresh_token=tokens['refresh_token'],
    user_id=tokens['user_id']
    )
items = client.get_items()
f2.close()

#check if basket is available
def ItemsAvailable():
    for i in items:        
        if 0 == i["items_available"]:            
            return "Il n'y a pas de panier disponible"
        else:
            list = []
            for i in items:
                if i["items_available"] != 0:
                    value = i["item"]["value_including_taxes"]["minor_units"]/100
                    newPrice = i["item"]["price_including_taxes"]["minor_units"]/100
                    item = {
                        "shop" : i["store"]["store_name"],
                        "number of item" : i["items_available"],
                        "value" : str(value)+"€",
                        "new price" : str(newPrice)+"€"
                    }
                    list.append(item)    
        return list
print(ItemsAvailable())




    

    