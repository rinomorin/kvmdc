import React, { useState } from 'react';
import './ServerContextMenu.css'; // Import your CSS file for styling

function ServerContextMenu({ x, y, onClose, onRegister, onUnregister, onStatus, onConsole, onReports }) {
  const handleClick = (action) => {
    onClose();
    switch (action) {
      case 'register':
        onRegister();
        break;
      case 'unregister':
        onUnregister();
        break;
      case 'status':
        onStatus();
        break;
      case 'console':
        onConsole();
        break;
      case 'reports':
        onReports();
        break;
      default:
        break;
    }
  };

  return (
    <div className="server-context-menu" style={{ top: y, left: x }}>
      <ul>
        <li onClick={() => handleClick('register')}>Register</li>
        <li onClick={() => handleClick('unregister')}>Unregister</li>
        <li onClick={() => handleClick('status')}>Status</li>
        <li onClick={() => handleClick('console')}>Console</li>
        <li onClick={() => handleClick('reports')}>Reports</li>
      </ul>
    </div>
  );
}

export default ServerContextMenu;
