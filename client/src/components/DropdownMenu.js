import React, { useState } from 'react';
import '../css/DropdownMenu.css'; // Import your CSS file

function DropdownMenu() {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const handleMenuItemClick = (action) => {
    console.log("Action:", action);
    setIsDropdownOpen(!isDropdownOpen)
    // Handle the action accordingly
  };

  return (
    <div className="dropdown">
      <div className="kebab-icon" onClick={() => setIsDropdownOpen(!isDropdownOpen)}>
        <span></span>
        <span></span>
        <span></span>
      </div>
      {isDropdownOpen && (
        <div className="dropdown-menu">
          <div onClick={() => handleMenuItemClick("Join")}>Join DC</div>
          <div onClick={() => handleMenuItemClick("Remove")}>Leave DC</div>
          <div onClick={() => handleMenuItemClick("Toggle")}>Toggle Node</div>
          <div onClick={() => handleMenuItemClick("Maintenance")}>Maintenance Node</div>
          <div onClick={() => handleMenuItemClick("About")}>About</div>
        </div>
      )}
    </div>
  );
}

export default DropdownMenu;