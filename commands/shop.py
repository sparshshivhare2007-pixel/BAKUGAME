from telegram import Update
from telegram.ext import CallbackContext

def shop_cmd(update: Update, context: CallbackContext):
    # Shop items yahan show karenge
    items = ["Sword - 50 coins", "Shield - 40 coins", "Potion - 10 coins"]
    shop_text = "🛒 Shop Items:\n" + "\n".join(items)
    update.message.reply_text(shop_text)
