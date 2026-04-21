from flask import Flask
import threading
import telebot
import os
import time

TOKEN = os.getenv("BOT_TOKEN")

web = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

@web.route('/')
def home():
    return "Bot is running!"

def run_bot():
    print("Bot started")

    bot.remove_webhook()
    time.sleep(1)

    bot.infinity_polling(skip_pending=True, none_stop=True)

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()

    port = int(os.getenv("PORT", 5000))
    web.run(host="0.0.0.0", port=port)