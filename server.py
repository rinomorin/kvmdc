from flask import Flask, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://192.168.100.3:27017/datacenter"
mongo = PyMongo(app)

client = MongoClient('mongodb://192.168.100.3:27017/')
db = client['datacenter']
# Replace 'your_database' with your actual database name


@app.route('/api/all_collections')
def get_all_collections():
    collections_data = {}
    for collection_name in db.list_collection_names():
        collections_data[collection_name] = list(db[collection_name].find({}, {'_id': 0}))
    return jsonify(collections_data)


@app.route('/api/hosts')
def get_nodes():
    hosts = list(mongo.db.hosts.find({}, {'_id': 0}))
    return jsonify(hosts)
# Exclude _id field from the result# Exclude _id field from the result


@app.route('/api/vms')
def get_vms():
    vms = list(mongo.db.members.find({}, {'_id': 0}))
    return jsonify(vms)
# Exclude _id field from the result


if __name__ == "__main__":
    #app.run(debug=True,host="0.0.0.0",port=5000)
    app.run(debug=True,port=5000)
