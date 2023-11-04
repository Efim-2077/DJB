#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
import settings
import utulis
import buttons
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        
        [InlineKeyboardButton(buttons.helloing1, callback_data="asw1")],
        [InlineKeyboardButton(buttons.helloing21, callback_data="asw2")],
        [InlineKeyboardButton(buttons.helloing31, callback_data="asw3")],
        [InlineKeyboardButton(buttons.helloing41, callback_data="asw4")],
        [InlineKeyboardButton(buttons.helloing51, callback_data="asw5")],
        [InlineKeyboardButton(buttons.helloing61, callback_data="asw6")],
        [InlineKeyboardButton(buttons.helloing71, callback_data="asw7")],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(utulis.reader(settings.PrepodBotka), reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    getback(update, context)

    
    # if query.data == 'asw1':
    #     asw = utulis.reader(settings.answer_1)
    
    # elif  query.data == 'asw2':
    #     asw = utulis.reader(settings.answer_2)
    # elif  query.data == 'asw3':
    #     asw = utulis.reader(settings.answer_3)
    # elif  query.data == 'asw4':
    #     asw = utulis.reader(settings.answer_4)
    # elif  query.data == 'asw5':
    #     asw = utulis.reader(settings.answer_5)
    # elif  query.data == 'asw6':
    #     asw = utulis.reader(settings.answer_6)
    # elif  query.data == 'asw7':
    #     asw = utulis.reader(settings.answer_7)
# {query.data} 

    await query.edit_message_text(text=settings.answers[query.data])


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")

async def getback(update, context):
    keyboard = [
        [InlineKeyboardButton("goo goo mack", callback_data=start(update, context))]
    ]
    


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6549929747:AAHsCBPgz87owE3-UnR8ANudxEM8m7XmNSs").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()