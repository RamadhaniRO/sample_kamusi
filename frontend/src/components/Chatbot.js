import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
  const [message, setMessage] = useState('');
  const [reply, setReply] = useState('');

  const handleSend = async () => {
    try {
      const response = await axios.post('http://localhost:5000/api/llm/chat', { message });
      setReply(response.data.reply);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Chatbot</h2>
      <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} />
      <button onClick={handleSend}>Send</button>
      <p>{reply}</p>
    </div>
  );
};

export default Chatbot;
