from economy import work
from database import create_user

def work_cmd(update, context):
    user_id = update.effective_user.id
    create_user(user_id)

    status, value = work(user_id)
    if status:
        update.message.reply_text(f"💼 You worked and earned 💰 {value} coins!")
    else:
        update.message.reply_text(f"⏳ Wait {value} seconds before working again!")
