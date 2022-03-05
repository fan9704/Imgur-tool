from imgurpython import ImgurClient
from dotenv import load_dotenv
load_dotenv()
import os 
import pyimgur
client_id =os.getenv("Client_ID")
client_secret =os.getenv("Client_secret")
client_name = os.getenv("Client Name")
# client = ImgurClient(client_id, client_secret)


# If you want to run this as a standalone script, so be it!
class Imgur:
    def __init__(self,client_id,client_name,client_secret):
        self.client_id=client_id
        self.client_name=client_name
        self.client_secret=client_secret

    def authenticate(self):
        self.client = ImgurClient(self.client_id, self.client_secret)
        authorization_url = self.client.get_auth_url('pin')
        print(f"Go to the following URL: {authorization_url}")
        pin = input("Enter pin code: ")
        credentials = self.client.authorize(pin, 'pin')
        self.client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
        print("Authentication successful! Here are the details:")
        print(f"   Access token:  {credentials['access_token']}")
        print(f"   Refresh token: {credentials['refresh_token']}")
        auth_tokens = {"access_token": credentials['access_token'],"refresh_token": credentials['refresh_token']}
        return self.client, auth_tokens

    def getImg(self,img_name):
        im = pyimgur.Imgur(client_id)
        image = im.get_image(img_name)
        print(image.title)
        print(image.link)
        return image.title,image.link

    def uploadImg(self,path):
        CLIENT_ID = self.client_id
        PATH = self.path #A Filepath to an image on your computer"
        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
        print(uploaded_image.title)
        print(uploaded_image.link)
        print(uploaded_image.type)
        return uploaded_image.title,uploaded_image.link,uploaded_image.type

    def getGallery(self):
        items = self.client.gallery()
        return [print(item) for item in items]
            

if __name__ == "__main__":
    imgur=Imgur(client_id=client_id,client_name=client_name,client_secret=client_secret)
    client , auth_token = imgur.authenticate()
    access_token = auth_token["access_token"]
    refresh_token = auth_token["refresh_token"]
    print(access_token,refresh_token)
    title,link=imgur.getImg("互換主權.png")
