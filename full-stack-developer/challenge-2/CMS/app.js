const express = require('express');
const bodyParser = require('body-parser');
const connectDB = require('./config/db');
const articleRoutes = require('./routes/articleRoutes');
const authRoutes = require('./routes/authRoutes');

const app = express();

// Connect to database
connectDB();

// Middleware
app.use(bodyParser.json());

// Routes
app.use('/api/articles', articleRoutes);
app.use('/api/auth', authRoutes);

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));