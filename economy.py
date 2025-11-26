from database import get_user, update_user
from utils import cooldown, reward
import time

def work(user_id):
    user = get_user(user_id)
    if not cooldown(user["last_work"], 60):
        remaining = 60 - (time.time() - user["last_work"])
        return (False, int(remaining))

    amount = reward(100, 200)
    update_user(user_id, "money", user["money"] + amount)
    update_user(user_id, "last_work", time.time())
    return (True, amount)

def daily(user_id):
    user = get_user(user_id)
    if not cooldown(user["last_daily"], 86400):
        remaining = 86400 - (time.time() - user["last_daily"])
        return (False, int(remaining))

    amount = reward(500, 1000)
    update_user(user_id, "money", user["money"] + amount)
    update_user(user_id, "last_daily", time.time())
    return (True, amount)
