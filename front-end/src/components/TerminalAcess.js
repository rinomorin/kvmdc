import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

const TerminalAccess = () => {
  const [ipAddress, setIpAddress] = useState('');
  const history = useHistory();

  const accessTerminal = async () => {
    try {
      // Send a POST request to the backend to access the terminal
      const response = await axios.post('/access-terminal', { ipAddress });
      
      // Open a new window with the terminal output
      const terminalWindow = window.open('', '_blank', 'width=800,height=600');
      terminalWindow.document.write(response.data);
    } catch (error) {
      console.error('Error accessing terminal:', error);
      alert('Error accessing terminal. Please try again.');
    }
  };

  return (
    <div>
      <h1>Web Terminal Access</h1>
      <input
        type="text"
        value={ipAddress}
        onChange={(e) => setIpAddress(e.target.value)}
        placeholder="Enter IP Address"
      />
      <button onClick={accessTerminal}>Access Terminal</button>
    </div>
  );
};

export default TerminalAccess;

