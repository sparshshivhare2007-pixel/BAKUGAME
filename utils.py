import random
import time

def cooldown(last_time, seconds):
    return time.time() - last_time >= seconds

def reward(amount_min, amount_max):
    return random.randint(amount_min, amount_max)
