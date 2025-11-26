from telegram.ext import Updater, CommandHandler
import os
from dotenv import load_dotenv

from database.database import create_user
from commands.work import work_cmd
from commands.daily import daily_cmd
from commands.profile import profile_cmd
from commands.rob import rob_cmd
from commands.shop import shop_cmd
from commands.buy import buy_cmd
from commands.leaderboard import leaderboard_cmd

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

def start(update, context):
    create_user(update.effective_user.id)
    update.message.reply_text(
        "🤖 Economy Bot Online!\nUse /work /daily /profile /rob /shop /buy /leaderboard"
    )

# Add all commands
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("work", work_cmd))
dp.add_handler(CommandHandler("daily", daily_cmd))
dp.add_handler(CommandHandler("profile", profile_cmd))
dp.add_handler(CommandHandler("rob", rob_cmd))
dp.add_handler(CommandHandler("shop", shop_cmd))
dp.add_handler(CommandHandler("buy", buy_cmd))
dp.add_handler(CommandHandler("leaderboard", leaderboard_cmd))

if __name__ == "__main__":
    print("🤖 Bot is starting...")
    updater.start_polling()
    updater.idle()
