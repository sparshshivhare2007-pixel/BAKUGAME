from database import get_user, create_user

def profile_cmd(update, context):
    user_id = update.effective_user.id
    create_user(user_id)
    user = get_user(user_id)

    text = (
        f"👤 Profile\n"
        f"Money: 💰 {user['money']}\n"
        f"Inventory: {', '.join(user['inventory']) if user['inventory'] else 'Empty'}"
    )
    update.message.reply_text(text)
