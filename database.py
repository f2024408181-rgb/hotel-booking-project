from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

print("DEBUG MONGO_URL:", MONGO_URL)  # add this line

client = MongoClient(MONGO_URL)

database = client.hotel_booking_db

booking_collection = database.bookings
