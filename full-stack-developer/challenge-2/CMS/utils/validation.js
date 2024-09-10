const { body, validationResult } = require('express-validator');

// Validation rules for articles
const articleValidationRules = () => [
  body('title').isString().withMessage('Title must be a string').notEmpty().withMessage('Title is required'),
  body('content').isString().withMessage('Content must be a string').notEmpty().withMessage('Content is required'),
  body('language').isIn(['en', 'bn']).withMessage('Language must be either "en" or "bn"'),
];

// Validation rules for user registration
const registerValidationRules = () => [
  body('username').isString().withMessage('Username must be a string').notEmpty().withMessage('Username is required'),
  body('password').isString().withMessage('Password must be a string').notEmpty().withMessage('Password is required').isLength({ min: 6 }).withMessage('Password must be at least 6 characters long'),
];

// Validation rules for user login
const loginValidationRules = () => [
  body('username').isString().withMessage('Username must be a string').notEmpty().withMessage('Username is required'),
  body('password').isString().withMessage('Password must be a string').notEmpty().withMessage('Password is required'),
];

// Middleware to check validation results
const validate = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }
  next();
};

module.exports = {
  articleValidationRules,
  registerValidationRules,
  loginValidationRules,
  validate,
};