import React, { useState, useEffect } from 'react';

function KvmDeviceList() {
  const [collections, setCollections] = useState([]);

  useEffect(() => {
    fetch('/api/collections')
      .then(response => response.json())
      .then(data => {
        console.log(data); // Handle the collections data
      })
      .catch(error => console.error('Error fetching collections:', error));
  }, []);

  // return (
  //   <div>
  //     <h1>Collections in database1</h1>
  //     {/* <ul>
  //       {collections.map((collection, index) => (
  //         <li key={index}>{collection.name}</li>
  //       ))}
  //     </ul> */}

  //   </div>
  // );
  // const [data, setData] = useState([]);

  // useEffect(() => {
  //   fetch('/api/data')
  //     .then(response => response.json())
  //     .then(data => setData(data))
  //     .catch(error => console.error('Error fetching data:', error));
  // }, []);

  // return (
  //   <div>
  //     <h1>Data from datacent</h1>
  //     <pre>{JSON.stringify(data, null, 2)}</pre>
  //   </div>
  // );

  // const [domainGroupsData, setDomainGroupsData] = useState([]);

  // useEffect(() => {
  //   fetch('/api/domain_groups_data')
  //     .then(response => response.json())
  //     .then(data => setDomainGroupsData(data))
  //     .catch(error => console.error('Error fetching domain groups data:', error));
  // }, []);

  // return (
  //   <div>
  //     <h2>Hosts</h2>
  //     <ul>
  //       {domainGroupsData.map(group => (
  //         <li key={group.domain}>
  //           <h3>{group.domain}</h3>
  //           <ul>
  //             {group.members.map(member => (
  //               <li key={member.host[0].name}>
  //                 <strong>Name:</strong> {member.host[0].name}<br />
  //                 <strong>IP:</strong> {member.host[0].ip}<br />
  //                 <strong>User ID:</strong> {member.host[0].user_id}<br />
  //                 <strong>Password:</strong> {member.host[0].password}<br />
  //                 <strong>Site:</strong> {member.host[0].site}<br />
  //               </li>
  //             ))}
  //           </ul>
  //         </li>
  //       ))}
  //     </ul>
  //   </div>
  // );
}

export default KvmDeviceList;