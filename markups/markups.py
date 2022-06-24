import time

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    markup = InlineKeyboardMarkup()
    s = InlineKeyboardButton(text='Мои обьявления', callback_data='user_advertisements')
    watch = InlineKeyboardButton(text='Смотреть объявления', callback_data='watch_adverts')
    add = InlineKeyboardButton(text='Добавить объявление', callback_data='add_advert')

    markup.add(s)
    markup.add(watch)
    markup.add(add)

    return markup


def advertisement_menu():
    markup = InlineKeyboardMarkup(row_width=2)

    delete_ad = InlineKeyboardButton(text='Удалить объявление', callback_data='delete_advertisements')
    add_ad = InlineKeyboardButton(text='Добавить объявление')

    markup.add(delete_ad)
    markup.add(add_ad)

    return markup


def menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    profile = KeyboardButton(text='ПРОФИЛЬ', callback_data='profile')

    markup.add(profile)

    return markup


def delete_advert():
    markup = InlineKeyboardMarkup(row_width=2)

    delete = InlineKeyboardButton(text='УДАЛИТЬ', callback_data='del_advert')

    markup.add(delete)

    return markup

