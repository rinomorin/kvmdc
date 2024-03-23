const express = require('express');
const mongoose = require('mongoose');
// const cors = require('cors');
const app = express();

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/datacenter', { useNewUrlParser: true });

// Define MongoDB schema and model
const domainGroupSchema = new mongoose.Schema({
  domain: String,
  members: [{ host: [{ name: String, ip: String, user_id: String, password: String, site: String }] }]
});

const DomainGroup = mongoose.model('DomainGroup', domainGroupSchema);

// API endpoint to fetch domain groups data
app.get('/api/domain_groups_data', async (req, res) => {
  try {
    const domainGroupsData = await DomainGroup.find();
    res.json(domainGroupsData);
  } catch (error) {
    console.error('Error fetching domain groups data:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get("/api/hosts", (req,  res) => {
    hosts = list(db.find({}, {'_id': 0}))
    return jsonify(hosts)
    // res.json(
    //     {domain_groups_data: [{
    //     "domain": "MorinSoft",
    //     "members": [
    //         {"host": [{"name": "morin-kvm01", "ip": "192.168.100.3", "user_id": "lv-user", "password": "password1", "site": "Site 1"}]},
    //         {"host": [{"name": "morin-kvm02", "ip": "192.168.100.4", "user_id": "lv-user", "password": "password1", "site": "Site 2"}]},
    //         {"host": [{"name": "morin-kvm03", "ip": "192.168.100.5", "user_id": "lv-user", "password": "password1", "site": "Site 3"}]}
    //     ]}
    // ]}
    // )
})
app.listen(4001,() => {console.log("server listening on port 4001")})
