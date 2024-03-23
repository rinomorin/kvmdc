const express = require('express');
const app = express();

app.get('/api', (req,  res) => {

    res.json({nodes: ["morin-kvm01","morin-kvm02","morin-kvm03"]})
})
app.listen(4001,() => {console.log("server listening on port 4001")})