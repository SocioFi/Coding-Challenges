const express = require('express');
const router = express.Router();
const articleController = require('../controllers/articleController');
const authMiddleware = require('../middleware/authMiddleware');
const { articleValidationRules, validate } = require('../utils/validation');

// Apply validation rules
router.post('/', authMiddleware, articleValidationRules(), validate, articleController.createArticle);
router.put('/:id', authMiddleware, articleValidationRules(), validate, articleController.updateArticle);

router.get('/', articleController.getArticles);
router.delete('/:id', authMiddleware, articleController.deleteArticle);

module.exports = router;