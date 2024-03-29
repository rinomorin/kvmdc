// App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ServerPopMenu from './ServerPopMenu';
import "../css/Nodes.css"
function KvmDeviceList() {
  const [hosts, setHosts] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:4001/api/hosts')
      .then(response => {
        setHosts(response.data);
      })
      .catch(error => {
        console.error('Error fetching hosts:', error);
      });
  }, []);

  return (
    <div>
    {hosts.map((domain,index) => (
        <ul className='DataCenter' data-header={"Datacenter ("+domain.domain+")"} key={index}>
        {domain.members.map((member, index) => (
          member.node.map((node, idx) => (
            <li key={index} value={node.ip}>
                  <strong><ServerPopMenu serverName={node.name} serverType="Host" /></strong>
            </li>
            ))
        ))}
        </ul>
    ))}
  </div>
  );
}

export default KvmDeviceList;
