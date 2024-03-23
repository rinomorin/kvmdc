import React, { useState, useEffect } from 'react';
import '../css/Nodes.css';
import ServerPopMenu from './ServerPopMenu';

function MyNodes() {
    const [nodes, setNodes] = useState([]);

    useEffect(() => {
        fetch('/api/hosts')
            .then(response => response.json())
            .then(data => setNodes(data))
            .catch(error => console.error('Error fetching nodes:', error));
    }, []);
    return (
        <div>
            {nodes.map((group, index) => (
                <ul className='DataCenter' data-header={"Datacenter ("+group.domain+")"} key={index}>
                    {group.members.map((member, index) => (
                        <li key={index} value={member.node[0].ip}>
                        <strong><ServerPopMenu serverName={member.node[0].name} serverType="Host" /></strong>
                        </li>
                    ))}
                </ul>
            ))}
        </div>
    );
}

function KVMNodes() {
    return (
        <div id="Nodes" className="KVMNodes">
            <MyNodes />
        </div>
    );
}

export default KVMNodes;
