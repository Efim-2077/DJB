import telebot
from telebot import types
import settings
import abouttime

# ABOUT_MSG = open('./about.txt')
# MSG_BASE_PATH = 'messages/'
# f = open('text.txt', 'r')

# with open(settings.FAQ['h1']) as file:
#    text = file.read()
#    print(text)


bot = telebot.TeleBot('6549929747:AAHsCBPgz87owE3-UnR8ANudxEM8m7XmNSs')

@bot.message_handler(commands=["start"])
def start(massege):
    markup = types.InlineKeyboardMarkup(row_width=1)
    helloing = types.InlineKeyboardButton(abouttime.helloing1, callback_data=abouttime.infoh1)
    helloing2 = types.InlineKeyboardButton(abouttime.helloing21, callback_data=abouttime.infoh2)
    helloing3 = types.InlineKeyboardButton(abouttime.helloing31, callback_data=abouttime.infoh3)
    helloing4 = types.InlineKeyboardButton(abouttime.helloing41, callback_data=abouttime.infoh4)
    helloing5 = types.InlineKeyboardButton(abouttime.helloing51, callback_data=abouttime.infoh5)
    helloing6 = types.InlineKeyboardButton(abouttime.helloing61, callback_data=abouttime.infoh6)
    helloing7 = types.InlineKeyboardButton(abouttime.helloing71, callback_data=abouttime.infoh7)
    markup.add(helloing, helloing2, helloing3, helloing4, helloing5, helloing6, helloing7)
    bot.send_message(massege.chat.id, abouttime.AnnaBotka, reply_markup=markup)



def getback():
    markup = types.InlineKeyboardMarkup(row_width=1)
    typayaliberostnya = types.InlineKeyboardButton("Вернутся в главное меню", callback_data="menu")
    #typayausa = types.InlineKeyboardButton("уууу бугиры и эйпфаны", callback_data="us")
    markup.add(typayaliberostnya)
    return markup

# faq = {'h1': 'hello.txt', 'h2': abouttime.helloing21}
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # faq = {'h1': 'hello.txt', 'h2': abouttime.helloing21}
    if call.message:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=[call.data],
            reply_markup=getback()
        )
    if call.message:
        if call.data == "menu":
            start(massege=call.message)




# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.message:
#         if call.data == "h1":
#             bot.edit_message_text(
#                chat_id=call.message.chat.id,
#                message_id=call.message.id,
#                text=infoh1,
#                reply_markup=getback()
#             )
#     if call.message:
#         if call.data == "h2":
#             bot.edit_message_text(
#                chat_id=call.message.chat.id,
#                message_id=call.message.id,
#                text=infoh2,
#                reply_markup=getback()
#             )
#     if call.message:
#         if call.data == "h3":
#             bot.edit_message_text(
#                chat_id=call.message.chat.id,
#                message_id=call.message.id,
#                text=infoh3,
#                reply_markup=getback()
#             )
#     if call.message:
#         if call.data == "h4":
#             bot.edit_message_text(
#                chat_id=call.message.chat.id,
#                message_id=call.message.id,
#                text=infoh4,
#                reply_markup=getback()
#             )
#     if call.message:
#         if call.data == "h5":
#             bot.edit_message_text(
#                chat_id=call.message.chat.id,
#                message_id=call.message.id,
#                text=infoh5,
#                reply_markup=getback()
#             )
#     if call.message:
#         if call.data == "h6":
#             bot.edit_message_text(
#                chat_id=call.message.chat.id,
#                message_id=call.message.id,
#                text=infoh6,
#                reply_markup=getback()
#             )
#     if call.message:
#         if call.data == "h7":
#             bot.edit_message_text(
#                chat_id=call.message.chat.id,
#                message_id=call.message.id,
#                text=infoh7,
#                reply_markup=getback()
#             )
    # if call.message:
    #     if call.data == "menu":
    #         start(massege=call.message)

bot.polling()