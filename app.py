from tgtg import TgtgClient
import json

#import of your tokens
f = open('token.json')
tokens = json.load(f)
client = TgtgClient(
    access_token=tokens['access_token'],
    refresh_token=tokens['refresh_token'],
    user_id=tokens['user_id']
    )
items = client.get_items()

#check if basket is available
def ItemsAvailable():
    for i in items:
        if i["items_available"] == 0:
            return "Il n'y a pas de panier disponible"
        else:
            list = []
            for i in items:
                if i["items_available"] != 0:
                    item = {
                        "shop" : i["store"]["store_name"],
                        "itemNumber" : i["items_available"]
                    }
                    list.append(item)    
        return list
print(ItemsAvailable())




    

    