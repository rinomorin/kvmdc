import React, { useState, useEffect } from 'react';

import '../css/Nodes.css';
import ServerPopMenu from './ServerPopMenu';

const HostsList = () => {
  const [hosts, setHosts] = useState([]);

  useEffect(() => {
    const fetchHosts = async () => {
      try {
        const response = await axios.get('http://192.168.0.1:5000/api/hosts');
        setHosts(response.data);
      } catch (error) {
        console.error('Error fetching hosts:', error);
      }
    };

    fetchHosts();
  }, []);

  return (
    <div>
      <h1>Hosts List</h1>
      <ul>
        {hosts.map((host, index) => (
          <li key={index}>
            <h2>{host.domain}</h2>
            <ul>
              {host.members.map((member, idx) => (
                <li key={idx}>
                  {member.node.map((node, i) => (
                    <div key={i}>
                      <p>Name: {node.name}</p>
                      <p>IP: {node.ip}</p>
                      <p>Password: {node.password}</p>
                      <p>Site: {node.site}</p>
                      <p>User ID: {node.user_id}</p>
                    </div>
                  ))}
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};


// function MyNodes() {
//     const [nodes, setNodes] = useState([]);

//     useEffect(() => {
//         const fetchJsonData = async () => {
//             try {
//               const response = await axios.get('http://192.168.100.3:5000/api/hosts');
//               setNodes(response.data);
//             } catch (error) {
//               console.error('Error fetching JSON data:', error);
//             }
//           };
                
//           fetchJsonData();

//         /** 
//          * const HostsList = () => {
//   const [hosts, setHosts] = useState([]);

//   useEffect(() => {
//     const fetchHosts = async () => {
//       try {
//         const response = await axios.get('http://192.168.0.1:5000/api/hosts');
//         setHosts(response.data);
//       } catch (error) {
//         console.error('Error fetching hosts:', error);
//       }
//     };

//     fetchHosts();
//   }, []);
//          * 
//          */
//         // fetch('/api/hosts')
//         //     .then(response => response.json())
//         //     .then(data => setNodes(data))
//         //     .catch(error => console.error('Error fetching nodes:', error));
//     }, []);
//     return (
//         <div>
//             {nodes.map((group, index) => (
//                 <ul className='DataCenter' data-header={"Datacenter ("+group.domain+")"} key={index}>
//                     {group.members.map((member, index) => (
//                         <li key={index} value={member.node[0].ip}>
//                         <strong><ServerPopMenu serverName={member.node[0].name} serverType="Host" /></strong>
//                         </li>
//                     ))}
//                 </ul>
//             ))}
//         </div>
//     );
// }

function KVMNodes() {
    return (
        <div id="Nodes" className="KVMNodes">
            <MyNodes />
        </div>
    );
}

export default KVMNodes;
