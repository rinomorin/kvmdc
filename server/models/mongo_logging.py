from pymongo import MongoClient
from bson import ObjectId  # Importing ObjectId class
from datetime import datetime


client = MongoClient('mongodb://localhost:27017/')
db = client['datacenter']
users_collection = db['users']
history_collection = db['history']
password_history_collection = db['password_history']
change_user = "mongodb admin"

pipeline = [{'$match': {'operationType': {
    '$in': ['insert', 'update', 'replace', 'delete']
    }}}]
try:
    with users_collection.watch(pipeline) as stream:
        for change in stream:
            history_collection.insert_one(change)

            # Log password changes to password_history
            if 'updateDescription' in change:
                updated_fields = change['updateDescription']['updatedFields']
                if 'password' in updated_fields:
                    old_password = updated_fields['password']
                    document_key = change['documentKey']
                    if '_id' in document_key:
                        user_data = users_collection.find_one(
                            {"_id": ObjectId(document_key['_id'])}
                            )
                        if user_data:
                            username = user_data.get("username")
                            last_password_change = user_data.get(
                                "last_password_change", datetime.now()
                                )
                            password_history_collection.insert_one({
                                "username": username,
                                "old_password": old_password,
                                "last_password_change": last_password_change,
                                "change_user": change_user,
                                "change_time": datetime.now()
                            })
                        else:
                            print("Error: User not found.")
                    else:
                        print("Error: '_id' not found in documentKey.")
except Exception as e:
    print("Error:", e)
