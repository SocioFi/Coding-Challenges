const chai = require('chai');
const chaiHttp = require('chai-http');
const server = require('../app');
const Article = require('../models/articleModel');

chai.should();
chai.use(chaiHttp);

describe('Articles', () => {
  beforeEach(async () => {
    await Article.deleteMany({});
  });

  describe('POST /api/articles', () => {
    it('should create a new article', (done) => {
      chai.request(server)
        .post('/api/articles')
        .send({ title: 'Test Article', content: 'This is a test article', language: 'en' })
        .end((err, res) => {
          res.should.have.status(201);
          res.body.should.have.property('message').eql('Article created');
          done();
        });
    });
  });

  describe('GET /api/articles', () => {
    it('should get all articles', (done) => {
      chai.request(server)
        .get('/api/articles')
        .end((err, res) => {
          res.should.have.status(200);
          res.body.should.be.a('array');
          done();
        });
    });
  });
});