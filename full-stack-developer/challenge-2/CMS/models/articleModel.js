const mongoose = require('mongoose');

const ArticleSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  content: {
    type: String,
    required: true,
  },
  language: {
    type: String,
    enum: ['en', 'bn'],
    required: true,
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

module.exports = mongoose.model('Article', ArticleSchema);