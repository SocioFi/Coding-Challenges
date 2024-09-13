const User = require('../models/userModel');
const jwt = require('jsonwebtoken');
const { secret, expiresIn } = require('../config/jwt');

exports.register = async (req, res) => {
  try {
    const { username, password } = req.body;
    const user = new User({ username, password });
    await user.save();
    res.status(201).json({ message: 'User registered' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

exports.login = async (req, res) => {
  try {
    const { username, password } = req.body;
    const user = await User.findOne({ username });
    if (!user || !(await user.matchPassword(password))) return res.status(401).json({ message: 'Invalid credentials' });

    const token = jwt.sign({ id: user._id }, secret, { expiresIn });
    res.status(200).json({ token });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};