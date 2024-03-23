const express = require('express');
const { MongoClient } = require('mongodb');
const app = express();

const client = new MongoClient(uri, { useUnifiedTopology: true });
const client = new MongoClient('mongodb://localhost:27017');
const dbName = 'datacenter';
client.connect((err) => {
    if (err) {
      console.error('Error connecting to MongoDB:', err);
      return;
    }
    console.log('Connected to MongoDB');
  
    const db = client.db(dbName);
    // Your MongoDB operations here
  });

app.get("/api/hosts", (req,  res) => {
    hosts = list(db.find({}, {'_id': 0}))
    return jsonify(hosts)
    // res.json({domain_groups_data: [{
    //     "domain": "MorinSoft",
    //     "members": [
    //         {"host": [{"name": "morin-kvm01", "ip": "192.168.100.3", "user_id": "lv-user", "password": "password1", "site": "Site 1"}]},
    //         {"host": [{"name": "morin-kvm02", "ip": "192.168.100.4", "user_id": "lv-user", "password": "password1", "site": "Site 2"}]},
    //         {"host": [{"name": "morin-kvm03", "ip": "192.168.100.5", "user_id": "lv-user", "password": "password1", "site": "Site 3"}]}
    //     ]}
    // ]})
})
app.listen(4001,() => {console.log("server listening on port 4001")})
