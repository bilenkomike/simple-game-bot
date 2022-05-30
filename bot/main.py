import telebot
from telebot import types
import random

bot=telebot.TeleBot("1842712437:AAHGT9LW3IJF6BQFIj6nlzk8mI6tgnkWxgI")




@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.tgs','rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Давай поиграем?!")
    item2 = types.KeyboardButton("Как дела?")
    markup.add(item1,item2)

    bot.send_message(message.chat.id, "Приветствую тебя, {0.first_name}!\n Мой дорогой друг, меня зовут - <b>{1.first_name}.\n Президент</b> этого чата!".format(message.from_user, bot.get_me()),
        parse_mode='html',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def getMessage(message):
    if message.chat.type == 'private':
        if message.text == 'Давай поиграем?!':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton('1', callback_data='1')
            item2 = types.InlineKeyboardButton('2', callback_data='2')
            item3 = types.InlineKeyboardButton('3', callback_data='3')
            item4 = types.InlineKeyboardButton('4', callback_data='4')
            item5 = types.InlineKeyboardButton('5', callback_data='5')
            item6 = types.InlineKeyboardButton('6', callback_data='6')
            item7 = types.InlineKeyboardButton('7', callback_data='7')
            item8 = types.InlineKeyboardButton('8', callback_data='8')
            item9 = types.InlineKeyboardButton('9', callback_data='9')
            item10 = types.InlineKeyboardButton('10', callback_data='10')

            markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10)
            bot.send_message(message.chat.id, 'Выбери число:', reply_markup=markup)
        elif message.text == 'Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Отлично! Сам как?", reply_markup=markup)
        else:
            sti1 = open('none.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti1)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            rand = str(random.randint(1, 11))


            if call.data == 'good':
                sti1 = open('sad.tgs', 'rb')
                bot.send_sticker(call.message.chat.id, sti1)
                bot.send_message(call.message.chat.id, "Тебе больше повезло! У меня 'Байден' пост президента увел \n во время выборов в 2020!")
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Может погираем?", reply_markup=None)
            elif call.data == 'bad':
                sti = open('happy.tgs', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, "Не ростраюйся! Я в той же яме, после выборов на пост президента в 2020!")
                # remove
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как дела?", reply_markup=None)

                # show alert
                # bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Пока!")
            else:
                if call.data == rand:
                    sti1 = open('win.tgs', 'rb')
                    bot.send_sticker(call.message.chat.id, sti1)
                    bot.send_message(call.message.chat.id, "Круто ты угодал число!\n И теперь на месяц ты получишь фирменное ничего!\n P.S. Не ростраюйся!😂")
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Может еще поиграем?", reply_markup=None)
                else:
                    sti1 = open('devillose.tgs', 'rb')
                    bot.send_sticker(call.message.chat.id, sti1)
                    bot.send_message(call.message.chat.id,
                                     ' - "Ну давай еще, <b>{0.first_name}</b>! Может где-то, там в другой галактике, ты выиграешь!\n Я в это искренне верю!" - 😄'.format(call.from_user, bot.get_me()), parse_mode='html',reply_markup=None)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Может еще поиграем?", reply_markup=None)



    except Exception as e:
        print(repr(e))



bot.polling(none_stop=True)