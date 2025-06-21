import pymongo

# Connect to MongoDB
client = pymongo.MongoClient('localhost', 27017)
db = client['octofit_db']

# Sample test data
test_users = [
    {"email": "alice@example.com", "name": "Alice", "age": 16, "team": "Red"},
    {"email": "bob@example.com", "name": "Bob", "age": 17, "team": "Blue"},
    {"email": "carol@example.com", "name": "Carol", "age": 16, "team": "Red"}
]

test_teams = [
    {"name": "Red", "members": ["alice@example.com", "carol@example.com"]},
    {"name": "Blue", "members": ["bob@example.com"]}
]

test_activities = [
    {"activity_id": 1, "user": "alice@example.com", "type": "run", "duration": 30, "points": 10},
    {"activity_id": 2, "user": "bob@example.com", "type": "walk", "duration": 60, "points": 8},
    {"activity_id": 3, "user": "carol@example.com", "type": "strength", "duration": 45, "points": 12}
]

test_leaderboard = [
    {"leaderboard_id": 1, "team": "Red", "points": 22},
    {"leaderboard_id": 2, "team": "Blue", "points": 8}
]

test_workouts = [
    {"workout_id": 1, "user": "alice@example.com", "description": "5k run"},
    {"workout_id": 2, "user": "bob@example.com", "description": "1 hour walk"},
    {"workout_id": 3, "user": "carol@example.com", "description": "Strength training"}
]

# Insert test data
db.users.insert_many(test_users)
db.teams.insert_many(test_teams)
db.activity.insert_many(test_activities)
db.leaderboard.insert_many(test_leaderboard)
db.workouts.insert_many(test_workouts)

print("Test data inserted successfully.")
