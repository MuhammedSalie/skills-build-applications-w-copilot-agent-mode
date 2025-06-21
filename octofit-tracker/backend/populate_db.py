import pymongo
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient('localhost', 27017)
db = client['octofit_db']

# Sample test data
users = [
    {"email": "alice@example.com", "name": "Alice", "age": 16, "team": "Red Rockets"},
    {"email": "bob@example.com", "name": "Bob", "age": 17, "team": "Blue Blazers"},
    {"email": "carol@example.com", "name": "Carol", "age": 15, "team": "Red Rockets"},
]

teams = [
    {"name": "Red Rockets", "members": ["alice@example.com", "carol@example.com"]},
    {"name": "Blue Blazers", "members": ["bob@example.com"]},
]

activities = [
    {"activity_id": 1, "user": "alice@example.com", "type": "run", "distance_km": 3.2, "date": datetime(2025, 6, 20)},
    {"activity_id": 2, "user": "bob@example.com", "type": "walk", "distance_km": 2.0, "date": datetime(2025, 6, 19)},
    {"activity_id": 3, "user": "carol@example.com", "type": "strength", "reps": 30, "date": datetime(2025, 6, 18)},
]

workouts = [
    {"workout_id": 1, "name": "Morning Cardio", "description": "30 min run and stretch"},
    {"workout_id": 2, "name": "Strength Circuit", "description": "Pushups, squats, lunges"},
]

leaderboard = [
    {"leaderboard_id": 1, "team": "Red Rockets", "points": 120},
    {"leaderboard_id": 2, "team": "Blue Blazers", "points": 90},
]

# Insert data only if collections are empty
if db.users.count_documents({}) == 0:
    db.users.insert_many(users)
if db.teams.count_documents({}) == 0:
    db.teams.insert_many(teams)
if db.activity.count_documents({}) == 0:
    db.activity.insert_many(activities)
if db.workouts.count_documents({}) == 0:
    db.workouts.insert_many(workouts)
if db.leaderboard.count_documents({}) == 0:
    db.leaderboard.insert_many(leaderboard)

print("Test data inserted into octofit_db.")
