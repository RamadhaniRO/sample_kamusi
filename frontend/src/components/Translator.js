import React, { useState } from 'react';
import { translateText } from '../api';

const Translator = () => {
  const [text, setText] = useState('');
  const [translatedText, setTranslatedText] = useState('');
  const [targetLang, setTargetLang] = useState('sw');

  const handleTranslate = async () => {
    const result = await translateText(text, targetLang);
    setTranslatedText(result.translatedText);
  };

  return (
    <div>
      <h2>Translator</h2>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <select value={targetLang} onChange={(e) => setTargetLang(e.target.value)}>
        <option value="sw">Swahili</option>
        <option value="en">English</option>
      </select>
      <button onClick={handleTranslate}>Translate</button>
      <p>{translatedText}</p>
    </div>
  );
};

export default Translator;
