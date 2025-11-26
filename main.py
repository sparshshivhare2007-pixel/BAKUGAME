from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv
from database import create_user
from commands.work import work_cmd
from commands.daily import daily_cmd
from commands.profile import profile_cmd
from commands.rob import rob_cmd
from commands.shop import shop_cmd
from commands.buy import buy_cmd
from commands.leaderboard import leaderboard_cmd

load_dotenv()  # .env file se variables load karega
TOKEN = os.getenv("BOT_TOKEN")

# Naya Application Builder use karenge (Updater ke jagah)
app = ApplicationBuilder().token(TOKEN).build()

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    create_user(update.effective_user.id)
    await update.message.reply_text(
        "🤖 Economy Bot Online!\nUse /work /daily /profile /rob /shop /buy /leaderboard"
    )

# Command handlers add karenge
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("work", work_cmd))
app.add_handler(CommandHandler("daily", daily_cmd))
app.add_handler(CommandHandler("profile", profile_cmd))
app.add_handler(CommandHandler("rob", rob_cmd))
app.add_handler(CommandHandler("shop", shop_cmd))
app.add_handler(CommandHandler("buy", buy_cmd))
app.add_handler(CommandHandler("leaderboard", leaderboard_cmd))

# Bot start karenge
app.run_polling()
