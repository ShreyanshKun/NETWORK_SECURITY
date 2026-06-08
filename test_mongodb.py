import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi

# 1. Load the hidden environment variables from your .env file
load_dotenv()

# 2. Securely fetch the URL
uri = os.getenv("MONGO_DB_URL")

# 3. Get the trusted security certificate to pass the cloud firewall
ca = certifi.where()

# 4. Create a new client, connect to the server, and pass the certificate!
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)