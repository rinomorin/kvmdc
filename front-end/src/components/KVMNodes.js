import React, { useState, useEffect } from 'react';
import axios from 'axios';
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
      {hosts.map((host, index) => (
      <ul className='DataCenter' data-header={"Datacenter ("+host.domain+")"} key={index}>            
            {host.members.map((member, idx) => (
            <li key={idx} value={member.ip}>
                   <strong><ServerPopMenu serverName={member.ip} serverType="Host" /></strong>
             </li>
              ))}
      </ul>
    ))}
    </div>
  );
};

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
            <HostsList />
        </div>
    );
}

export default KVMNodes;
