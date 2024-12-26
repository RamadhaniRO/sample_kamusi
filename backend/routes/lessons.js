const express = require('express');
const Lesson = require('../models/Lesson');
const router = express.Router();

router.get('/', async (req, res) => {
  try {
    const lessons = await Lesson.find();
    res.json(lessons);
  } catch (error) {
    res.status(500).json({ error: 'Server error' });
  }
});

module.exports = router;
