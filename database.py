import sqlite3
import os

# Database file location
DB_FILE = "database/economy.db"

# Ensure database folder exists
if not os.path.exists("database"):
    os.makedirs("database")

# Connect to database and create table if not exists
conn = sqlite3.connect(DB_FILE, check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    coins INTEGER DEFAULT 100,
    daily_claimed INTEGER DEFAULT 0
)
""")
conn.commit()

# ----------------------------
# Functions for bot
# ----------------------------

def create_user(user_id):
    """Add a new user to the database if not exists"""
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = c.fetchone()
    if not user:
        c.execute("INSERT INTO users (user_id, coins) VALUES (?, ?)", (user_id, 100))
        conn.commit()

def get_coins(user_id):
    """Return current coins of a user"""
    c.execute("SELECT coins FROM users WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    if result:
        return result[0]
    return 0

def add_coins(user_id, amount):
    """Add coins to a user"""
    create_user(user_id)
    c.execute("UPDATE users SET coins = coins + ? WHERE user_id = ?", (amount, user_id))
    conn.commit()

def remove_coins(user_id, amount):
    """Remove coins from a user"""
    create_user(user_id)
    c.execute("UPDATE users SET coins = coins - ? WHERE user_id = ? AND coins >= ?", (amount, user_id, amount))
    conn.commit()

def claim_daily(user_id):
    """Mark daily claimed"""
    create_user(user_id)
    c.execute("SELECT daily_claimed FROM users WHERE user_id = ?", (user_id,))
    last_claimed = c.fetchone()[0]
    if last_claimed == 0:
        c.execute("UPDATE users SET coins = coins + 50, daily_claimed = 1 WHERE user_id = ?", (user_id,))
        conn.commit()
        return True
    return False

def reset_daily():
    """Reset daily claim for all users (run every 24h if needed)"""
    c.execute("UPDATE users SET daily_claimed = 0")
    conn.commit()
