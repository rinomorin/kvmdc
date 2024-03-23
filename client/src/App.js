import React, {useEffect, useState} from 'react'

function App() {
  const [BackendData, setBackendData] = useState[{}]

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
   </div>
  )
}

export default App 

