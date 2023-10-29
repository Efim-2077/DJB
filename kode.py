import telebot
from telebot import types
import settings
import buttons
import utulis

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
    helloing = types.InlineKeyboardButton(buttons.helloing1, callback_data=utulis.reader(settings.answer_1))
    helloing2 = types.InlineKeyboardButton(buttons.helloing21, callback_data=utulis.reader(settings.answer_2))
    helloing3 = types.InlineKeyboardButton(buttons.helloing31, callback_data=utulis.reader(settings.answer_3))
    helloing4 = types.InlineKeyboardButton(buttons.helloing41, callback_data=utulis.reader(settings.answer_4))
    helloing5 = types.InlineKeyboardButton(buttons.helloing51, callback_data=utulis.reader(settings.answer_5))
    helloing6 = types.InlineKeyboardButton(buttons.helloing61, callback_data=utulis.reader(settings.answer_6))
    helloing7 = types.InlineKeyboardButton(buttons.helloing71, callback_data=utulis.reader(settings.answer_7))
    otherQ = types.InlineKeyboardButton(buttons.otherQtext, callback_data=utulis.reader(settings.mycont))
    wannabot = types.InlineKeyboardButton(buttons.wannatext, callback_data=utulis.reader(settings.ifuwanna))
    markup.add(helloing, helloing2, helloing3, helloing4, helloing5, helloing6, helloing7, otherQ, wannabot)
    bot.send_message(massege.chat.id, utulis.reader(settings.PrepodBotka),reply_markup=markup)



def getback():
    markup = types.InlineKeyboardMarkup(row_width=1)
    typayaliberostnya = types.InlineKeyboardButton("Вернутся в главное меню", callback_data="menu")
    #typayausa = types.InlineKeyboardButton("уууу бугиры и эйпфаны", callback_data="us")
    markup.add(typayaliberostnya)
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
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




bot.polling()