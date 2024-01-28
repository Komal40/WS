// MyComponent.js

// import React, { useEffect, useState } from 'react';
// import axios from 'axios';

// const MyComponent = () => {
//   const [objectData, setObjectData] = useState({ name: 'Loading...', status: 'Loading...' });

//   useEffect(() => {
//     // Fetch data from the API endpoint
//     axios.get('http://localhost:5000/api/object_data')
//       .then(response => {
//         setObjectData(response.data);
//       })
//       .catch(error => {
//         console.error('Error fetching data:', error);
//       });
//   }, []); // Empty dependency array means useEffect runs once on component mount

//   return (
//     <div>
//       <h1>Object Status:</h1>
//       <p>Name: {objectData.name}, Status: {objectData.status}</p>
//     </div>
//   );
// };

// export default MyComponent;





// MyComponent.js


import React, { useEffect, useState } from 'react';
import socketIOClient from 'socket.io-client';

const MyComponent = () => {
  const [objectData, setObjectData] = useState({ name: 'Loading...', status: 'Loading...' });

  useEffect(() => {
    // http://127.0.0.1:5000
    const socket = socketIOClient('http://localhost:5000', {
        transports: ['websocket'],
        withCredentials: true,  // Add this line
      });

    socket.on('update_object', (data) => {
      console.log('Received object update:', data);
      setObjectData(data);
    });

    return () => {
      socket.disconnect(); // Cleanup on component unmount
    };
  }, []); // Empty dependency array means useEffect runs once on component mount

  return (
    <div>
      <h1>Object Status:</h1>
      <p>Name: {objectData.name}, Status: {objectData.status}</p>
    </div>
  );
};

export default MyComponent;

