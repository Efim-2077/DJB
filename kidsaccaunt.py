
import schedule
import time
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

async def les(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="GGPOXEROK")















def job():
    print("Выполняются действия по расписанию")

schedule.every().saturday.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)