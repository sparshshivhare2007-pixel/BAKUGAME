from telegram import Update
from telegram.ext import CallbackContext

def profile_cmd(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    # Fetch user profile from database
    coins = 100  # Example value
    update.message.reply_text(f"👤 Profile of {user_id}\n💰 Coins: {coins}")
