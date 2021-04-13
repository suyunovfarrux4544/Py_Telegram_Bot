import telebot
import os
import requests
from telebot.types import (
    InlineKeyboardButton, ReplyKeyboardMarkup,
    KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove)

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
data = {}



@bot.message_handler(commands=['start'])
def start_message(message):
    text = f"Assalomu alaykum kompaniyamizga hush kelibsiz"
    reply_markup = InlineKeyboardMarkup(
        row_width=1)
    reply_markup.add(
        InlineKeyboardButton(text="Registrasiyadan otish", callback_data="reg_user")
    )

    bot.send_message(message.from_user.id, text, reply_markup=reply_markup)

@bot.callback_query_handler(func=lambda c: True)
def callback_message(callback):
    if callback.data == 'reg_user':
        text = 'Korxonangiz nomini kiriting !'
        data['step'] = 'region'
        bot.send_message(callback.from_user.id, text)

@bot.message_handler(func=lambda m: True)
def text_messsage(message):
    user_step = data.get('step')
    if user_step == 'region':
        data['company_name'] = message.text
        data['step'] = 'adres'
        text = f"Korxona nomi:{data.get('company_name')}\n\n"
        text += 'Qaysi hududda faoliyat olib borasiz'
        reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        reply_markup.add(*[
            KeyboardButton(text='Buxoro'),
            KeyboardButton(text='Navoiy'),
            KeyboardButton(text='Qarshi')
        ])

        bot.send_message(message.from_user.id, text, reply_markup=reply_markup)

    elif user_step == 'adres':
        data['region'] = message.text
        data['step'] = 'orientor'
        text = "Manzilizni kiriting, iltimos"
        bot.send_message(message.from_user.id, text)

    elif user_step == 'orientor':
        data['adres'] = message.text
        data['step'] = 'phone'
        text = "Manzilingiz joylashgan mo'ljalingizni kiriting"
        bot.send_message(message.from_user.id, text)

    elif user_step == 'phone':
        data['orientor'] = message.text
        data['step'] = 'phone2'
        text = "Telefon nomerizni kiriting!"
        bot.send_message(message.from_user.id, text)


    elif user_step == 'phone2':
        data['phone'] = message.text
        data['step'] = 'end'
        text = "Qushimch telefon raqamingizni kiriting"
        bot.send_message(message.from_user.id, text)

    elif user_step == 'end':
        data['phone2'] = message.text
        text = f"hayr sog buling\n\n{data}"
        bot.send_message(message.from_user.id, text)


bot.polling(none_stop=True)