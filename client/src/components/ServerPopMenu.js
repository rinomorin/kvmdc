import React, { useState, useEffect, useRef } from 'react';
import '../css/ServerPopMenu.css'; // Import your CSS file for styling
// import KvmShell from './KvmShell';

function ServerPopMenu({ serverName, serverType }) {
  const [menuVisible, setMenuVisible] = useState(false);
  const [menuPosition, setMenuPosition] = useState({ x: 0, y: 0 });
  const menuRef = useRef(null);
  const KvmShell = require('./KvmShell');

  useEffect(() => {
    function handleClickOutside(event) {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setMenuVisible(false);
      }
    }

    document.addEventListener('click', handleClickOutside);

    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  }, []);

  const handleContextMenu = (event) => {
    event.preventDefault();
    setMenuPosition({ x: event.clientX, y: event.clientY });
    setMenuVisible(true);
  };

  const handleClick = () => {
    setMenuVisible(!menuVisible);
  };
  
  let options;
  switch (serverType) {
    case 'Host':
      options = ['Connect', 'Disconnect', 'Remove', 'Status', KvmShell.KvmShell('127.0.0.1'), 'Reports'];
      break;
    case 'VM':
      options = ['edit', 'console', 'reports', 'power up', 'power down', 'pause'];
      break;
    default:
      options = [];
  }

  return (
    <div className="server-menu" ref={menuRef}>
      <div className="server-name" onContextMenu={handleContextMenu} onClick={handleClick}>{serverName}</div>
      {menuVisible && (
        <div className="menu" style={{ top: menuPosition.y, left: menuPosition.x }}>
          <ul>
          {/* serverType */}
          {options.map((option, index) => (
              <li key={index} onClick={() => handleClick(option)}>{option}</li>
            )
          )}
          </ul>
        </div>
      )}
    </div> 
  );
}

export default ServerPopMenu;
