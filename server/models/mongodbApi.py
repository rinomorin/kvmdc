import pymongo
import psutil
import subprocess
from models.kvmconfig import KVMDC_Config
from models.kvmconfig import KVMdcConfig


class MongoDBManager:
    Mongo_attribs = {}

    def __init__(self):
        # mongo = {}
        dbi = KVMdcConfig
        dbtoken = KVMDC_Config['dbm']['Authorization']
        connection_string = dbi.get_item_from_token(self, dbtoken, 'dbcon')
        database_name = dbi.get_item_from_token(self, dbtoken, 'dbname')
        self.connection_string = connection_string
        self.database_name = database_name
        self.client = None
        self.db = None

    def __setitem__(self, key, value):
        self.Mongo_attribs[key] = value

    def __getitem__(self, key):
        return self.Mongo_attribs[key]

    def __delitem__(self, key):
        self.Mongo_attribs[key] = None

    def connect(self):
        try:
            if not self.client:
                self.client = pymongo.MongoClient(self.connection_string)
                self.db = self.client[self.database_name]
                # self.database = self.client.get_database()
                print("Connected to MongoDB")
            return self.client
        except pymongo.errors.ConnectionFailure as e:
            print("Could not connect to MongoDB:", e)

    def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None
            print("Disconnected from MongoDB")

    def insert_one(self, collection_name, document):
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(document)
            print("Inserted document:", result.inserted_id)
            return result.inserted_id
        except Exception as e:
            print("Error inserting document:", e)

    def find_one(self, collection_name, query):
        try:
            collection = self.db[collection_name]
            print("query",query)
            result = collection.find_one(query)
            print("Found document:", result)
            return result
        except Exception as e:
            print("Error finding document:", e)

    def get_collection_list(self):
        # Get the list of collections in the connected database
        collection_list = self.database.list_collection_names()
        return collection_list

    def is_collection_in_list(self, collection_name):
        # Check if the given collection name is in the list
        collection_list = self.get_collection_list()
        return collection_name in collection_list

    def count_collections(self):
        # Count the number of collections in the database
        # collection_count = self.database.list_collection_names()
        collection_count = self.db.list_collection_names()
        return len(collection_count)

    def close_connection(self):
        # Close the MongoDB connection
        self.client.close()

    def is_process_running(self, process_name):
        for process in psutil.process_iter():
            if process.name() == process_name:
                return True
        return False

    def start_external_script(self, script_path):
        print("starting db logging")
        subprocess.Popen(["python", script_path])
        
    def update_login_key(self, id, newKey):
        pass


db = MongoDBManager()
