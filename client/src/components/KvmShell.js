import React from 'react';
import axios from 'axios';

const KvmShellComponent = () => {
  const handleOpenShellClick = () => {
    axios.post('/api/kvm-shell') // Make API call to backend
      .then(response => {
        console.log('KVM shell opened successfully:', response.data);
        // Handle successful response (e.g., display shell output in frontend)
      })
      .catch(error => {
        console.error('Error opening KVM shell:', error);
        // Handle error
      });
  };

  return (
    <li onClick={handleOpenShellClick}></li>
      <h1>KVM Shell</h1>
      <button onClick={handleOpenShellClick}>Open KVM Shell</button>
    </li>
  );
};

export default KvmShellComponent;