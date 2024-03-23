import React, { useState, useEffect }  from 'react';

export const kvmDeviceList =() => {
    const [backendData, setBackendData]  = useState([]);

    useEffect(() => {
      fetch("/api/hosts").then(
        response => response.json()
      ).then(
        data => {
          setBackendData(data)
        }
      )
    }, [])
    return (
    <div>  
      {typeof backendData.nodes === 'undefined' ? (
         <p>Loading nodes...</p>
      ):(
        backendData.nodes.map((node,i) => {
            <p key={i}>{node.name}</p>
        })
      )}  
    </div>
    )
}