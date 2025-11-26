from database import load_data

def leaderboard_cmd(update, context):
    data = load_data()
    lb = sorted(data.items(), key=lambda x: x[1]["money"], reverse=True)

    text = "🏆 Leaderboard:\n"
    for i, (uid, info) in enumerate(lb[:10], 1):
        text += f"{i}. User {uid} → 💰 {info['money']}\n"

    update.message.reply_text(text)
