from tgtg import TgtgClient
# Pour récupérer les tokens
# Ajouter l'email
client = TgtgClient(email="email")
credentials = client.get_credentials()

print(credentials)