const express = require('express');
// const MongoClient = require('mongodb').MongoClient;
const mongoose = require('mongoose');
// const cors = require('cors');
const app = express();
// app.use(cors());

// MongoDB connection URL
const url = 'mongodb://localhost:27017';
const dbName = 'datacenter';

// const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/datacenter')
.then(() => console.log('MongoDB connected'))
.catch(err => console.error(err));


// In your Express route handler
app.get('/api/database', async (req, res) => {
    try {
      // Fetch all documents from all collections in the database
      const collections = await mongoose.connection.db.collections();
      const data = {};
  
      for (const collection of collections) {
        const documents = await collection.find({}).toArray();
        data[collection.collectionName] = documents;
      }
  
      res.json(data);
    } catch (err) {
      console.error(err);
      res.status(500).json({ error: 'Internal server error' });
    }
  });

 app.get('/api/hosts', async (req, res) => {
    try {
      // Fetch all documents from all collections in the database
      const collections = await mongoose.connection.db.collections();
      const data = {};
  
      for (const collection of collections) {
        const documents = await collection.find({}).toArray();
        data[collection.collectionName] = documents;
      }
  
      res.json(data);
    } catch (err) {
      console.error(err);
      res.status(500).json({ error: 'Internal server error' });
    }
  });


app.listen(4001,() => {console.log("server listening on port 4001")})
