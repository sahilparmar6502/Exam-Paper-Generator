📂 question-service/ (Stores & Retrieves Questions)
🔹 Purpose: This service is responsible for storing, managing, and retrieving questions from the MongoDB database.
🔹 APIs:

GET /questions → Fetches all questions
POST /questions → Adds new questions
GET /questions?topic=DSA&difficulty=hard → Retrieves specific questions
🔹 Database: Connects to MongoDB, storing questions with fields like:

🔹 Why separate this service?
It allows scalability—other services (like generation-service/) can fetch questions without worrying about data storage.