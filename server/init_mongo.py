from pymongo import MongoClient

# MongoDB connection settings
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Initialize MongoDB client
client = MongoClient(MONGO_HOST, MONGO_PORT)

# Access or create the database
db = client['datacenter']

# Create user collection with specified schema
user_collection = db['users']
user_schema = {
    "sid": {"bsonType": "string"},
    "username": {"bsonType": "string"},
    "password": {"bsonType": "string"},
    "salutation": {"bsonType": "string"},
    "first_name": {"bsonType": "string"},
    "last_name": {"bsonType": "string"},
    "employee_serial_number": {"bsonType": "string"},
    "employee_email": {"bsonType": "string"},
    "employee_phone": {"bsonType": "string"},
    "employee_country": {"bsonType": "string"},
    "company": {"bsonType": "string"},
    "employee_manager_name": {"bsonType": "string"},
    "employee_manager_email": {"bsonType": "string"},
    "employee_manager_phone": {"bsonType": "string"},
    "employee_secret": {"bsonType": "string"},
    "status": {"bsonType": "string"}
}
user_collection.create_index("sid", unique=True)
user_collection.create_index("username", unique=True)

# Create log history collection
log_collection = db['log_history']

# Define change stream pipeline
pipeline = [
    {"$match": {"operationType": {
        "$in": ["insert", "update", "replace", "delete"]
        }}}
]

# Create change stream on user collection
with user_collection.watch(pipeline) as stream:
    for change in stream:
        print(change)  # Here you can define your logic to handle changes
