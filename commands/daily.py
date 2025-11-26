from telegram import Update
from telegram.ext import CallbackContext

def daily_cmd(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    # Daily reward logic yahan
    update.message.reply_text(f"📅 User {user_id} collected their daily reward!")
