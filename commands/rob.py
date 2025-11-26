from telegram import Update
from telegram.ext import CallbackContext

def rob_cmd(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    # Rob logic yahan
    update.message.reply_text(f"🏴 User {user_id} tried to rob someone but failed!")
