import React, { useState } from 'react';

const VoiceRecognition = () => {
  const [transcript, setTranscript] = useState('');

  const startListening = () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = 'sw-SW'; // Swahili
    recognition.onresult = (event) => {
      setTranscript(event.results[0][0].transcript);
    };
    recognition.start();
  };

  return (
    <div>
      <h2>Voice Recognition</h2>
      <button onClick={startListening}>Start Listening</button>
      <p>{transcript}</p>
    </div>
  );
};

export default VoiceRecognition;
