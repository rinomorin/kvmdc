import json
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["datacenter"] 
collection = db["vms"]

# Query for all nodes
all_nodes = collection.find()

# Convert nodes to JSON and print
print("All Nodes:")
for node in all_nodes:
    print(json.dumps(node, default=str)) 