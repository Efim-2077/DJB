import telebot
from telebot import types
import settings
from abouttime import helloing1, helloing21, helloing31, helloing41, helloing51, helloing61, helloing71, AnnaBotka, infoh1, infoh2, infoh3, infoh4, infoh5, infoh6, infoh7

#ABOUT_MSG = open('about.txt')
#MSG_BASE_PATH = 'messages/'
#f = open('text.txt', 'r')
 
bot = telebot.TeleBot('6549929747:AAHsCBPgz87owE3-UnR8ANudxEM8m7XmNSs')

@bot.message_handler(commands=["start"])
def start(massege):
    markup = types.InlineKeyboardMarkup(row_width=1)
    helloing = types.InlineKeyboardButton(helloing1, callback_data="h1")
    helloing2 = types.InlineKeyboardButton(helloing21, callback_data="h2")
    helloing3 = types.InlineKeyboardButton(helloing31, callback_data="h3")
    helloing4 = types.InlineKeyboardButton(helloing41, callback_data="h4")
    helloing5 = types.InlineKeyboardButton(helloing51, callback_data="h5")
    helloing6 = types.InlineKeyboardButton(helloing61, callback_data="h6")
    helloing7 = types.InlineKeyboardButton(helloing71, callback_data="h7")
    markup.add(helloing, helloing2, helloing3, helloing4, helloing5, helloing6, helloing7)
    bot.send_message(massege.chat.id, AnnaBotka, reply_markup=markup)


def getback():
    markup = types.InlineKeyboardMarkup(row_width=1)
    typayaliberostnya = types.InlineKeyboardButton("Вернутся в главное меню", callback_data="menu")
    #typayausa = types.InlineKeyboardButton("уууу бугиры и эйпфаны", callback_data="us")
    markup.add(typayaliberostnya)
    return markup




 
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "h1":
            bot.edit_message_text(
               chat_id=call.message.chat.id,
               message_id=call.message.id,
               text=infoh1,
               reply_markup=getback()
            )
    if call.message:
        if call.data == "h2":
            bot.edit_message_text(
               chat_id=call.message.chat.id,
               message_id=call.message.id,
               text=infoh2,
               reply_markup=getback()
            )
    if call.message:
        if call.data == "h3":
            bot.edit_message_text(
               chat_id=call.message.chat.id,
               message_id=call.message.id,
               text=infoh3,
               reply_markup=getback()
            )
    if call.message:
        if call.data == "h4":
            bot.edit_message_text(
               chat_id=call.message.chat.id,
               message_id=call.message.id,
               text=infoh4,
               reply_markup=getback()
            )
    if call.message:
        if call.data == "h5":
            bot.edit_message_text(
               chat_id=call.message.chat.id,
               message_id=call.message.id,
               text=infoh5,
               reply_markup=getback()
            )
    if call.message:
        if call.data == "h6":
            bot.edit_message_text(
               chat_id=call.message.chat.id,
               message_id=call.message.id,
               text=infoh6,
               reply_markup=getback()
            )
    if call.message:
        if call.data == "h7":
            bot.edit_message_text(
               chat_id=call.message.chat.id,
               message_id=call.message.id,
               text=infoh7,
               reply_markup=getback()
            )










    if call.message:
        if call.data == "menu":
            start(massege=call.message)




bot.polling()