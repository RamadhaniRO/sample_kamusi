const express = require('express');
const { pipeline } = require('@huggingface/transformers');
const router = express.Router();

// Load a pre-trained model
const translator = pipeline('translation_en_to_sw', 'Helsinki-NLP/opus-mt-en-sw');
const chatbot = pipeline('conversational', 'microsoft/DialoGPT-medium');

router.post('/translate', async (req, res) => {
  const { text } = req.body;
  try {
    const result = await translator(text);
    res.json({ translatedText: result[0].translation_text });
  } catch (error) {
    res.status(500).json({ error: 'Translation failed' });
  }
});

router.post('/chat', async (req, res) => {
  const { message } = req.body;
  try {
    const result = await chatbot(message);
    res.json({ reply: result[0].generated_text });
  } catch (error) {
    res.status(500).json({ error: 'Chat failed' });
  }
});

module.exports = router;
