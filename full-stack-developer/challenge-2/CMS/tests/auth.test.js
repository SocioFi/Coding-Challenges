const chai = require('chai');
const chaiHttp = require('chai-http');
const server = require('../app');
const User = require('../models/userModel');

chai.should();
chai.use(chaiHttp);

describe('Auth', () => {
  beforeEach(async () => {
    await User.deleteMany({});
  });

  describe('POST /api/auth/register', () => {
    it('should register a new user', (done) => {
      chai.request(server)
        .post('/api/auth/register')
        .send({ username: 'testuser', password: 'testpassword' })
        .end((err, res) => {
          res.should.have.status(201);
          res.body.should.have.property('message').eql('User registered');
          done();
        });
    });
  });

  describe('POST /api/auth/login', () => {
    it('should login a user', (done) => {
      chai.request(server)
        .post('/api/auth/login')
        .send({ username: 'testuser', password: 'testpassword' })
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.have.property('token');
          done();
        });
    });
  });
});