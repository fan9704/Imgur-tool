from imgurpython import ImgurClient
from dotenv import load_dotenv
load_dotenv()
import os 
client_id =os.get.env("Client_ID")
client_secret =os.get.env("Client_secret")
client_name = os.get.env("Client Name")
client = ImgurClient(client_id, client_secret)

# Example request
items = client.gallery()
for item in items:
    print(item.link)
