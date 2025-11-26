from economy import daily
from database import create_user

def daily_cmd(update, context):
    user_id = update.effective_user.id
    create_user(user_id)

    status, value = daily(user_id)
    if status:
        update.message.reply_text(f"🎁 You claimed your daily reward: 💰 {value} coins!")
    else:
        update.message.reply_text(f"⏳ Wait {value//3600} hours before daily reward!")
