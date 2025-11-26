from telegram import Update
from telegram.ext import CallbackContext

def leaderboard_cmd(update: Update, context: CallbackContext):
    # Example leaderboard
    leaderboard = [
        "User1 - 500 coins",
        "User2 - 400 coins",
        "User3 - 300 coins"
    ]
    text = "🏆 Leaderboard:\n" + "\n".join(leaderboard)
    update.message.reply_text(text)
