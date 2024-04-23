from pymongo import MongoClient


class MongoDB:
    # mongo = []
    def __init__(self):
        self.mongo = {}

    def __getitem__(self, key):
        if key in self.mongo:
            return self.mongo[key]
        else:
            return None

    def __setitem__(self, key, value):
        self.mongo[key] = value

    def MongoConnect(self):
        try:
            client = MongoClient(self.mongo['mongo_url'])
            db = client[self.mongo['mongo_client']]
            return db
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return None
