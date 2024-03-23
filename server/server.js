const express = require('express');
const app = express();

app.get("/api/hosts", (req,  res) => {
    res.json({domain_groups_data: [{
        "domain": "MorinSoft",
        "members": [
            {"host": [{"name": "morin-kvm01", "ip": "192.168.100.3", "user_id": "lv-user", "password": "password1", "site": "Site 1"}]},
            {"host": [{"name": "morin-kvm02", "ip": "192.168.100.4", "user_id": "lv-user", "password": "password1", "site": "Site 2"}]},
            {"host": [{"name": "morin-kvm03", "ip": "192.168.100.5", "user_id": "lv-user", "password": "password1", "site": "Site 3"}]}
        ]}
    ]})
})
app.listen(4001,() => {console.log("server listening on port 4001")})

// domain_groups_data = [
//     {
//         "domain": "MorinSoft",
//         "members": [
//             {"node": [{"name": "Node1", "ip": "192.168.1.100", "user_id": "admin", "password": "password1", "site": "laptop"}]},
//             {"node": [{"name": "Node2", "ip": "192.168.1.101", "user_id": "admin", "password": "password2", "site": "plex"}]},
//             {"node": [{"name": "Node3", "ip": "192.168.1.102", "user_id": "admin", "password": "password3", "site": "kvm"}]}
//         ]
//     }
// ]