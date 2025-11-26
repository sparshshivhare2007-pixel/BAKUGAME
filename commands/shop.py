def shop_cmd(update, context):
    items = [
        "Laptop - 5000 coins",
        "Bike - 20000 coins",
        "Car - 50000 coins"
    ]
    update.message.reply_text("🛒 Shop:\n" + "\n".join(items))
