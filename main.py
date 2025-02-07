import os
from telegram.ext import Application
from handlers import *
from dotenv import load_dotenv

load_dotenv()

def main():
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("Token do bot não configurado!")

    app = Application.builder().token(bot_token).build()
    
    # Configure os handlers
    app.add_handler(CommandHandler("start", start))
    # Adicione outros handlers...
    
    app.run_polling()

if __name__ == "__main__":
    main()