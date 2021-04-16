from telebot.types import (
    ReplyKeyboardMarkup, InlineKeyboardMarkup,
    KeyboardButton, InlineKeyboardButton)

# def registrasiya():
#     reply_markup = InlineKeyboardMarkup(
#         row_width=1)
#     reply_markup.add(
#         InlineKeyboardButton(text="Registrasiyadan otish", callback_data='Ha')
#     )
#     return reply_markup

def Region():
    reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=2)
    reply_markup.add(*[
        KeyboardButton(text='Buxoro'),
        KeyboardButton(text='Navoiy'),
        KeyboardButton(text='Qarshi'),
    ])
    return reply_markup

def Buxoro_region():
    reply_markup = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True)
    reply_markup.add(*[
        KeyboardButton(text='Kogon'),
        KeyboardButton(text='Peshku'),
        KeyboardButton(text='Buxoro'),
        KeyboardButton(text='Gijduvon'),
        KeyboardButton(text='Olot'),
        KeyboardButton(text='Jondor'),
        KeyboardButton(text='Qorakol'),
        KeyboardButton(text='Qoravulbozor'),
        KeyboardButton(text='Romitan'),
        KeyboardButton(text='Shofikron'),
        KeyboardButton(text='Vobkent')
    ])
    return reply_markup

def Navoiy_region():
    reply_markup=ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True
    )
    reply_markup.add(*[
        KeyboardButton(text='Konimex'),
        KeyboardButton(text='Nurota'),
        KeyboardButton(text='Navbahor'),
        KeyboardButton(text='Qiziltepa'),
        KeyboardButton(text='Navoiy'),
        KeyboardButton(text='Xatirchi'),
        KeyboardButton(text='Tomdi')
    ])
    return reply_markup

def Qashqadaryo_region():
    reply_markup=ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True
    )
    reply_markup.add(*[
        KeyboardButton(text='Qarshi'),
        KeyboardButton(text='Guzor'),
        KeyboardButton(text='Koson'),
        KeyboardButton(text='Kitob'),
        KeyboardButton(text='Qamashi'),
        KeyboardButton(text='Nishon'),
        KeyboardButton(text='Kasbi'),
        KeyboardButton(text='Muborak'),
        KeyboardButton(text='Yakkabog'),
        KeyboardButton(text='Shahrisabz'),
        KeyboardButton(text='Dehqonobod'),
        KeyboardButton(text='Mirishkor'),
        KeyboardButton(text='Chiroqchi')
    ])
    return reply_markup