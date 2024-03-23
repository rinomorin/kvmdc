import React, { useState, useEffect }  from 'react';
from pymongo import MongoClient;

function  KvmDeviceList () {
    const [backendData, setBackendData]  = useState([{}]);

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
      {(typeof backendData.hosts === 'undefined') ? (
         <p>Loading hosts...</p>
      ) : (
        backendData.hosts.map((host, i) => (<p key={i}>{host}</p>))
      )}  
    </div>
    );
}

export default KvmDeviceList;