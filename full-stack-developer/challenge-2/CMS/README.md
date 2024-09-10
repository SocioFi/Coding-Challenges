
# CMS API for News Website

## Overview

This is a Node.js and Express.js API for managing news articles in Bangla and English. It supports CRUD operations, authentication, and input validation.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```
2.	Install Dependencies:
```bash
npm install
```
3. Start the Server:
```bash
npm run dev
```
4. Access the API:
 Open your browser or use Postman at http://localhost:5001.

#### Postman Collection

.	Import the Collection:
	•	Open Postman.
	•	Click “Import”.
	•	Choose Postman/PostmanCollections.json from the postman folder.
.	Use the Collection:
Test various API endpoints included in the collection.

### API Endpoints

	•	POST /api/articles - Create an article.
	•	GET /api/articles - Get all articles or filter by language.
	•	GET /api/articles/:id - Get an article by ID.
	•	PUT /api/articles/:id - Update an article.
	•	DELETE /api/articles/:id - Delete an article.
	•	POST /api/auth/register - Register a user.
	•	POST /api/auth/login - Login and get a JWT token