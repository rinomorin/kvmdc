// import React, { useState, useEffect, useRef } from 'react';
// import '../css/ServerPopMenu.css'; // Import your CSS file for styling
// function ServerType({ serverName, serverType,y,x }) {
//     const [menuVisible, setMenuVisible] = useState(false);
//     const [menuPosition, setMenuPosition] = useState({ x: 0, y: 0 });
//     const menuRef = useRef(null);
  
//     useEffect(() => {
//       function handleClickOutside(event) {
//         if (menuRef.current && !menuRef.current.contains(event.target)) {
//           setMenuVisible(false);
//         }
//       }
  
//       document.addEventListener('click', handleClickOutside);
//       return () => {
//         document.removeEventListener('click', handleClickOutside);
//       };
//     }, []);
  
//     const handleContextMenu = (event) => {
//       event.preventDefault();
//       setMenuPosition({ x: event.clientX, y: event.clientY });
//       setMenuVisible(true);
//     };
  
//     const handleClick = () => {
//       setMenuVisible(!menuVisible);
//     };
  
//     let options;
//     switch (serverType) {
//       case 'host':
//         options = ['register', 'unregister', 'status', 'console', 'reports'];
//         break;
//       case 'vm':
//         options = ['register', 'unregister', 'status', 'console', 'reports', 'power up', 'power down'];
//         break;
//       default:
//         options = [];
//     }
//     return (
//         <div className="server-context-menu" style={{ top: y, left: x }}>
//           <ul>
//             {options.map((option, index) => (
//               <li key={index} onClick={() => handleClick(option)}>{option}</li>
//             ))}
//           </ul>
//         </div>
//       );
//       top: menuPosition.y, left: menuPosition.x
// };

// export default ServerType;