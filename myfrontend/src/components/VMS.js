// VMs.js
import React, { useState, useEffect } from 'react';

const VMS = () => {
  const [vms, setVMS] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://192.168.100.3:5000/api/vms');
        const data = await response.json();
        setVMS(data);
      } catch (error) {
        console.error('Error fetching VMS:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>VMs List</h2>
      <ul>
        {vms.map((vm, index) => (
          <li key={index}>
            {/* Render VM data */}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default VMS;
