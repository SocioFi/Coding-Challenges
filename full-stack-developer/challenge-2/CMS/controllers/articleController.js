const Article = require('../models/articleModel');

exports.createArticle = async (req, res) => {
  try {
    const { title, content, language } = req.body;
    const article = new Article({ title, content, language });
    await article.save();
    res.status(201).json({ message: 'Article created', article });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

exports.getArticles = async (req, res) => {
  try {
    const language = req.query.language;
    const articles = language ? await Article.find({ language }) : await Article.find();
    res.status(200).json(articles);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

exports.updateArticle = async (req, res) => {
  try {
    const { id } = req.params;
    const { title, content, language } = req.body;
    const article = await Article.findByIdAndUpdate(id, { title, content, language }, { new: true });
    if (!article) return res.status(404).json({ message: 'Article not found' });
    res.status(200).json({ message: 'Article updated', article });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

exports.deleteArticle = async (req, res) => {
  try {
    const { id } = req.params;
    const article = await Article.findByIdAndDelete(id);
    if (!article) return res.status(404).json({ message: 'Article not found' });
    res.status(200).json({ message: 'Article deleted' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};