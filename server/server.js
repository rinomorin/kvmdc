const express = require('express');
const MongoClient = require('mongodb').MongoClient;
// const mongoose = require('mongoose');
// const cors = require('cors');
const app = express();

// MongoDB connection URL
const url = 'mongodb://localhost:27017';
const dbName = 'datacenter';

// Connect to MongoDB
MongoClient.connect(url, (err, client) => {
    if (err) {
      console.error('Error connecting to MongoDB:', err);
      return;
    }
    console.log('Connected to MongoDB');
  
    const db = client.db(dbName);
  
    // API endpoint to fetch data from database1
    app.get('/api/data', async (req, res) => {
      try {
        const data = await db.collection('collection1').find({}).toArray();
        res.json(data);
      } catch (error) {
        console.error('Error fetching data:', error);
        res.status(500).json({ error: 'Error fetching data' });
      }
    });
  });

// Connect to MongoDB
// mongoose.connect('mongodb://localhost:27017/datacenter');

// app.get("/api/hosts", (req,  res) => {
//     hosts = list(db.find({}, {'_id': 0}))
//     return jsonify(hosts)
//     // res.json(
//     //     {domain_groups_data: [{
//     //     "domain": "MorinSoft",
//     //     "members": [
//     //         {"host": [{"name": "morin-kvm01", "ip": "192.168.100.3", "user_id": "lv-user", "password": "password1", "site": "Site 1"}]},
//     //         {"host": [{"name": "morin-kvm02", "ip": "192.168.100.4", "user_id": "lv-user", "password": "password1", "site": "Site 2"}]},
//     //         {"host": [{"name": "morin-kvm03", "ip": "192.168.100.5", "user_id": "lv-user", "password": "password1", "site": "Site 3"}]}
//     //     ]}
//     // ]}
//     // )
// })
app.listen(4001,() => {console.log("server listening on port 4001")})
