const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const server = http.createServer(app);

// Initialize Socket.io with reconnection logic
const io = socketIO(server, {
  reconnectionAttempts: 5, // Retry 5 times
  reconnectionDelay: 2000,  // Wait 2 seconds between retries
});

app.use(cors());
app.use(express.json());

mongoose.connect('mongodb://localhost/chatDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const chatSchema = new mongoose.Schema({
  username: String,
  message: String,
  image: String, // for image messages
  timestamp: { type: Date, default: Date.now },
});

const Chat = mongoose.model('Chat', chatSchema);

io.on('connection', (socket) => {
  console.log('New user connected');

  socket.on('sendMessage', async (data) => {
    const newMessage = new Chat(data);
    await newMessage.save();
    io.emit('receiveMessage', data);
  });

  socket.on('typing', (data) => {
    socket.broadcast.emit('typing', data);
  });

  socket.on('disconnect', () => {
    console.log('User disconnected');
  });
});

app.get('/chatHistory', async (req, res) => {
  const history = await Chat.find().sort({ timestamp: -1 }).limit(50);
  res.json(history);
});

const PORT = process.env.PORT || 5002;
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));