from telegram import Bot
from config import BOT_TOKEN, CHANNEL_USERNAME
from fetch_sofascore import fetch_live_tennis_matches
import schedule
import time
import random

bot = Bot(token=BOT_TOKEN)
sent_ids = set()

betting_phrases = [
    "🔥 Hot Pick!",
    "🎯 Sharp Bet!",
    "⚡ Quick Tip!",
    "💸 Smart Move!",
    "🧠 Expert Insight!",
    "📈 Trending Now!",
    "✅ Safe Bet!",
    "🤑 Value Pick!"
]

def post_live_matches():
    matches = fetch_live_tennis_matches()
    for match in matches:
        if match['id'] not in sent_ids:
            phrase = random.choice(betting_phrases)
            msg = f"🎾 {match['tournament']} – {match['match']}\n📊 Status: {match['score']}\n{phrase}"
            bot.send_message(chat_id=CHANNEL_USERNAME, text=msg)
            sent_ids.add(match['id'])

schedule.every(1).minutes.do(post_live_matches)

print("🤖 Bot is running...")

while True:
    schedule.run_pending()
    time.sleep(1)
