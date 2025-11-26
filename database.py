import json
import os

DB_PATH = "data/users.json"

def load_data():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)

def create_user(user_id):
    data = load_data()
    if str(user_id) not in data:
        data[str(user_id)] = {
            "money": 0,
            "inventory": [],
            "last_daily": 0,
            "last_work": 0
        }
        save_data(data)

def get_user(user_id):
    data = load_data()
    return data.get(str(user_id), None)

def update_user(user_id, key, value):
    data = load_data()
    data[str(user_id)][key] = value
    save_data(data)
