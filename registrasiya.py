from telebot.types import (
    ReplyKeyboardMarkup,InlineKeyboardMarkup,
    KeyboardButton,InlineKeyboardButton)

def registrasiya():
    reply_markup = InlineKeyboardMarkup(
        row_width=1)
    reply_markup.add(
        InlineKeyboardButton(text="Registrasiyadan otish", callback_data='Ha')
    )
    return reply_markup

def Hudud():
    reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=2)
    reply_markup.add(*[
        KeyboardButton(text='Toshkent'),
        KeyboardButton(text='Samarqand'),
        KeyboardButton(text='Qarshi'),
        KeyboardButton(text='Andijon')
    ])