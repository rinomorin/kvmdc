// server.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();
const PORT = process.env.PORT || 4001;

app.use(cors());
app.use(express.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/datacenter');
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

// Define a schema for the hosts collection
const hostSchema = new mongoose.Schema({
  domain: String,
  members: [
    {
      node: {
        name: String,
        ip: String
      }
    }
  ]
});

const guestSchema = new mongoose.Schema({
  nodes: String,
  members:[
    {
      vm: {
        name: String,
        ip: String
      }
    }
  ]
});

// Define a model for the hosts collection
const Host   = mongoose.model('Host', hostSchema);
const Member = mongoose.model('Member', guestSchema);
// Define a route to fetch hosts from the database
app.get('/api/hosts', async (req, res) => {
  try {
    const hosts = await Host.find();
    res.json(hosts);
  } catch (err) {
    console.error('Error fetching hosts:', err);
    res.status(500).json({ message: 'Internal server error' });
  }
});

app.get('/api/guests', async (req, res) => {
  try {
    const guests = await Member.find();
    res.json(guests);
  } catch (err) {
    console.error('Error fetching guests:', err);
    res.status(500).json({ message: 'Internal server error' });
  }
});
// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
