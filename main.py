import telebot
import os
from Regions import *
import requests
from telebot.types import (
    InlineKeyboardButton, ReplyKeyboardMarkup,
    KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove)

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
data = {}



@bot.message_handler(commands=['start'])
def start_message(message):
    text = f"Assalomu alaykum kompaniyamizga hush kelibsiz\n"
    text += "Viloyatingizni kiriting"
    data['step'] = 'region'
    bot.send_message(message.from_user.id, text, reply_markup=Region())

# @bot.callback_query_handler(func=lambda c: True)
# def callback_message(callback):
#     if callback.data == 'reg_user':
#         text = 'Korxonangiz nomini kiriting !'
#         data['step'] = 'region'
#         bot.send_message(callback.from_user.id, text)

@bot.message_handler(func=lambda m: True)
def text_messsage(message):
    user_step = data.get('step')
    if message.text == 'Buxoro' and user_step == 'region':
        text="Tumaningiz nomini kiriting ! "
        data['step'] = 'company_name'
        bot.send_message(message.from_user.id,text, reply_markup=Buxoro_region())

    elif message.text == 'Navoiy' and user_step == 'region':
        text = "Tumaningiz nomini kiriting ! "
        data['step'] = 'company_name'
        bot.send_message(message.from_user.id, text,reply_markup=Navoiy_region())

    elif message.text == 'Qarshi' and user_step == 'region':
        text = "Tumaningiz nomini kiriting ! "
        data['step'] = 'company_name'
        bot.send_message(message.from_user.id, text, reply_markup=Qashqadaryo_region())

    elif user_step == 'company_name':
        data['region'] = message.text
        data['step'] = 'phone'
        text = "Korxonangiz nomini kiriting "
        bot.send_message(message.from_user.id, text,reply_markup=ReplyKeyboardRemove())


    elif user_step == 'phone':
        data['company_name'] = message.text
        data['step'] = 'phone2'
        text = "Telefon nomerizni kiriting!"
        bot.send_message(message.from_user.id, text)


    elif user_step == 'phone2':
        data['phone'] = message.text
        data['step'] = 'end'
        text = "Qushimcha telefon raqamingizni kiriting"
        bot.send_message(message.from_user.id, text)

    elif user_step == 'end':
        data['phone2'] = message.text
        text = f"Hayr sog buling\n\n{data}"
        bot.send_message(message.from_user.id, text)


bot.polling(none_stop=True)