import os
os.system('cls')

print("======= Welcome to Sports Inventory Management =======")

# Database configuration
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://monsur:z8ve7sfrdk@inventory.lykf5oo.mongodb.net/?retryWrites=true&w=majority"

mclient = MongoClient(uri)
