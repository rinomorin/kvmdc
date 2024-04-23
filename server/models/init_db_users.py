import pymongo
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timedelta

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['datacenter']
users_collection = db['users']
history_collection = db['history']
password_history_collection = db['password_history']
change_user = "mongodb admin"

# Define the schema for the users collection
schema = {
    "username": {"type": "string", "unique": True},
    "password": "string",
    "token": "string",
    "salutation": "string",
    "first_name": "string",
    "last_name": "string",
    "employee_serial_number": "string",
    "employee_email": "string",
    "employee_phone": "string",
    "employee_country": "string",
    "company": "string",
    "employee_manager_name": "string",
    "employee_manager_email": "string",
    "employee_manager_phone": "string",
    "login_key": "string",
    "status": "string",
    "last_login": "date",
    "last_logout": "date",
    "last_password_change": "date",
    "expire_date": "date",
    "fail_count": "int",
    "fail_time": "date"
}

# Create the users collection with the defined schema
users_collection.create_index([("username", pymongo.ASCENDING)], unique=True)

# Add a test user to the collection
test_user = {
    "username": "test_user",
    "password": "testPassWord",
    "token": None,
    "salutation": "",
    "first_name": "test",
    "last_name": "user",
    "employee_serial_number": "",
    "employee_email": "root@localhost.ca",
    "employee_phone": "1 (000) 000-0000",
    "employee_country": "Canada",
    "company": "test ltd",
    "employee_manager_name": "testmanage",
    "employee_manager_email": "mgr_mail",
    "employee_manager_phone": "1 (000) 000-0000",
    "login_key": None,
    "status": "disabled",
    "last_login": datetime.now(),
    "last_logout": None,
    "last_password_change": datetime.now() - timedelta(days=1),
    "expire_date": datetime.now() + timedelta(days=1),
    "fail_count": 5,
    "fail_time": datetime.now() - timedelta(minutes=5)
}

try:
    users_collection.insert_one(test_user)
    print("Test user added successfully.")
except pymongo.errors.DuplicateKeyError:
    print("Error: Username already exists.")
except Exception as e:
    print("Error:", e)


# Define the change stream to trigger a log update
pipeline = [{'$match': {'operationType': {
    '$in': ['insert', 'update', 'replace', 'delete']
    }}}]
try:
    with users_collection.watch(pipeline) as stream:
        for change in stream:
            history_collection.insert_one(change)
            print("Change logged:", change)

            # Log password changes to password_history
            if 'updateDescription' in change:
                updated_fields = change['updateDescription']['updatedFields']
                if 'password' in updated_fields:
                    old_password = updated_fields['password']
                    document_key = change['documentKey']
                    if '_id' in document_key:
                        user_data = users_collection.find_one({
                            "_id": ObjectId(document_key['_id'])
                            })
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

print("Database setup completed.")
