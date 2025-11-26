from telegram import Update
from telegram.ext import CallbackContext

def work_cmd(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    # Yahan aap database logic dal sakte ho
    update.message.reply_text(f"💼 User {user_id} did some work and earned coins!")
