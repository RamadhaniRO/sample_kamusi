const express = require('express');
const { OpenAI } = require('openai');
const router = express.Router();

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

router.post('/generate-lesson', async (req, res) => {
  const { topic } = req.body;
  try {
    const response = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a Swahili language tutor.' },
        { role: 'user', content: `Create a lesson on ${topic} in Swahili. Include a quiz.` },
      ],
    });
    res.json({ lesson: response.choices[0].message.content });
  } catch (error) {
    res.status(500).json({ error: 'Failed to generate lesson' });
  }
});

router.post('/chat', async (req, res) => {
  const { message } = req.body;
  try {
    const response = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a Swahili language assistant.' },
        { role: 'user', content: message },
      ],
    });
    res.json({ reply: response.choices[0].message.content });
  } catch (error) {
    res.status(500).json({ error: 'Failed to generate reply' });
  }
});

module.exports = router;
