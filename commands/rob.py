import random
from database import get_user, update_user, create_user

def rob_cmd(update, context):
    user_id = update.effective_user.id
    create_user(user_id)

    if not context.args:
        update.message.reply_text("Usage: /rob <username>")
        return
    
    victim_name = context.args[0]
    update.message.reply_text("Robbing is not fully implemented yet!")
