import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["datacenter"]  # Replace "your_database_name" with your actual database name
collection = db["nodes"]
db["nodes"].drop()
collection = db["hosts"]
domain_groups_data = [
    {
        "domain": "MorinSoft",
        "members": [
            {"node": [{"name": "Node1", "ip": "192.168.1.100", "user_id": "admin", "password": "password1", "site": "laptop"}]},
            {"node": [{"name": "Node2", "ip": "192.168.1.101", "user_id": "admin", "password": "password2", "site": "plex"}]},
            {"node": [{"name": "Node3", "ip": "192.168.1.102", "user_id": "admin", "password": "password3", "site": "kvm"}]}
        ]
    }
]

# Insert node information into the collection
collection.insert_many(domain_groups_data)

collection = db["vms"]
node_vm = [
    {
        "nodes": "Node1",
        "members": [
            {"vm": [{"name": "node1-vm01", "ip": "192.168.1.110", "user_id": "sysadmin", "password": "password1", "site": "laptop"}]},
            {"vm": [{"name": "node1-vm02", "ip": "192.168.1.111", "user_id": "sysadmin", "password": "password2", "site": "laptop"}]},
            {"vm": [{"name": "node1-vm02", "ip": "192.168.1.112", "user_id": "sysadmin", "password": "password3", "site": "laptop"}]}
        ]
    },
    {
        "nodes": "Node2",
        "members": [
            {"vm": [{"name": "node2-vm01", "ip": "192.168.1.120", "user_id": "sysadmin", "password": "password1", "site": "plex"}]},
            {"vm": [{"name": "node2-vm02", "ip": "192.168.1.121", "user_id": "sysadmin", "password": "password2", "site": "plex"}]},
            {"vm": [{"name": "node2-vm03", "ip": "192.168.1.122", "user_id": "sysadmin", "password": "password3", "site": "plex"}]}
        ]
    },
    {
        "nodes": "Node3",
        "members": [
            {"vm": [{"name": "node3-vm01", "ip": "192.168.1.130", "user_id": "sysadmin", "password": "password1", "site": "kvm"}]},
            {"vm": [{"name": "node3-vm02", "ip": "192.168.1.131", "user_id": "sysadmin", "password": "password2", "site": "kvm"}]},
            {"vm": [{"name": "node3-vm03", "ip": "192.168.1.132", "user_id": "sysadmin", "password": "password3", "site": "kvm"}]}
        ]
    }
]
collection.insert_many(node_vm)

print("Node information inserted successfully.")

query = {"name": {"$regex": "Node.*"}}  # Filter condition to find documents where the name starts with "Node"
update = {"$set": {"new_field": "new_value"}}  # New field and value to add
update = {"$set": {"domain": "MorinSoft"}}  # New field and value to add
collection.update_many(query, update)