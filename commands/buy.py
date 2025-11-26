from telegram import Update
from telegram.ext import CallbackContext

def buy_cmd(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    args = context.args
    if not args:
        update.message.reply_text("Usage: /buy <item_name>")
        return
    item = " ".join(args)
    # Database me item purchase logic
    update.message.reply_text(f"🛍️ User {user_id} bought {item}!")
