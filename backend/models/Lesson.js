const mongoose = require('mongoose');

const lessonSchema = new mongoose.Schema({
  title: { type: String, required: true },
  content: { type: String, required: true },
  quiz: [
    {
      question: String,
      options: [String],
      answer: String,
    },
  ],
});

module.exports = mongoose.model('Lesson', lessonSchema);
