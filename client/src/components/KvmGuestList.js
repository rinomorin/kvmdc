// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ServerPopMenu from './ServerPopMenu';
import "../css/Nodes.css"
function KvmGuestList() {
  const [guests, setHosts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:4001/api/guests')
      .then(response => {
        setHosts(response.data);
      })
      .catch(error => {
        console.error('Error fetching hosts:', error);
      });
  }, []);

  return (
    <div>
    <ul className='DataCenter' data-header="vms">
    {guests.map((guest,index) => (
        guest.members.map((member, index) => (
          member.vm.map((vm, idx) => (
          <li key={index} value={vm.ip}>
          <strong><ServerPopMenu serverName={vm.name} serverType="VM" /></strong>
          </li>
          ))
        ))
    ))}
    </ul>
  </div>
  );
}

export default KvmGuestList;
