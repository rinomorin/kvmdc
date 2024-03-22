// Hosts.js
import React, { useState, useEffect } from 'react';

const Hosts = () => {
  const [hosts, setHosts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://cors-anywhere.herokuapp.com/http://192.168.100.3:5000/api/hosts');
        const data = await response.json();
        setHosts(data);
      } catch (error) {
        console.error('Error fetching hosts:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>Hosts List</h2>
      <ul>
        {hosts.map((host, index) => (
          <li key={index}>
            {/* Render host data */}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Hosts;
