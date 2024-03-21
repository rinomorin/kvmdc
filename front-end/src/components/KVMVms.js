import React, { useState, useEffect } from 'react';
import '../css/Nodes.css';
import ServerPopMenu from './ServerPopMenu';
function MyVms() {
    const [nodes, setNodes] = useState([]);

    useEffect(() => {
        fetch('/api/vms')
            .then(response => response.json())
            .then(data => setNodes(data))
            .catch(error => console.error('Error fetching nodes:', error));
    }, []);

    return (
        <div>
            <ul className='DataCenter' data-header="vms">
                {nodes.map((group, index) => (
                    group.members.map((member, index) => (
                        <React.Fragment key={index}>
                            {member.vm.map((vm, vmIndex) => (
                                <li key={vmIndex} value={vm.ip}>
                                <strong><ServerPopMenu serverName={vm.name} serverType="VM" /></strong>
                                </li>
                            ))}
                        </React.Fragment>
                    ))
                ))}
            </ul>
        </div>
    );
}

function KVMVms() {
    return (
        <div id="KVMVms" className="LeftSide">
            <MyVms />
        </div>
    );
}

export default KVMVms;
