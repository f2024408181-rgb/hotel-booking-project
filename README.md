# Hotel Booking Project

A hotel booking form built with FastAPI and MongoDB.

## Tech Stack
- FastAPI
- MongoDB Atlas
- Jinja2 Templates
- HTML/CSS

## Setup

1. Clone the repository
2. Create a virtual environment:
python -m venv .venv
.venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Create a `.env` file and add your MongoDB URL:
MONGO_URL=your_mongodb_url_here
5. Run the project:
uvicorn main:app --reload
6. Open `http://127.0.0.1:8000` in your browser

## Features
- Hotel booking form with full name, email, phone, check-in/out dates, room type, guests, and special requests
- Data stored in MongoDB Atlas
- Clean and responsive UI