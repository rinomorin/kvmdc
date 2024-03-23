import React, { useState, useEffect } from 'react';

function KvmDeviceList() {
  const [domainGroupsData, setDomainGroupsData] = useState([]);

  useEffect(() => {
    fetch('/api/domain_groups_data')
      .then(response => response.json())
      .then(data => setDomainGroupsData(data))
      .catch(error => console.error('Error fetching domain groups data:', error));
  }, []);

  return (
    <div>
      <h2>Hosts</h2>
      <ul>
        {domainGroupsData.map(group => (
          <li key={group.domain}>
            <h3>{group.domain}</h3>
            <ul>
              {group.members.map(member => (
                <li key={member.host[0].name}>
                  <strong>Name:</strong> {member.host[0].name}<br />
                  <strong>IP:</strong> {member.host[0].ip}<br />
                  <strong>User ID:</strong> {member.host[0].user_id}<br />
                  <strong>Password:</strong> {member.host[0].password}<br />
                  <strong>Site:</strong> {member.host[0].site}<br />
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default KvmDeviceList;