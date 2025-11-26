from database import get_user, update_user

def buy_cmd(update, context):
    if not context.args:
        update.message.reply_text("Usage: /buy <item>")
        return

    item = context.args[0].capitalize()
    user_id = update.effective_user.id
    user = get_user(user_id)

    prices = {"Laptop": 5000, "Bike": 20000, "Car": 50000}

    if item not in prices:
        update.message.reply_text("Item not found!")
        return

    if user["money"] < prices[item]:
        update.message.reply_text("Not enough money!")
        return

    user["money"] -= prices[item]
    user["inventory"].append(item)
    update_user(user_id, "money", user["money"])
    update_user(user_id, "inventory", user["inventory"])

    update.message.reply_text(f"✅ You bought {item}!")
