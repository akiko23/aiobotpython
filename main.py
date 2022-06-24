from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from functions import bot_commands

import markups.markups2 as nav

from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher import FSMContext

from selenium import webdriver

from functions.advert_functions import *
from functions.sub_functions import *
from states import ConvertStates, Pay_sub

from pyqiwip2p import QiwiP2P
from gtts import gTTS
from pathlib import Path
from functions.convert import *

from db import Database
from states.UserStates import FSMAdmin
from config import *

import markups.markups as nav2
from states import ConvertStates
from config import UKASSA_TOKEN
import functions

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}

sticker_list = ['CAACAgIAAxkBAAEFEPhirG9xzTQ8SQG1n5YmdGayJUz8ygAC_xAAAr1h0EvxMyHBHEIYxiQE',
                'CAACAgIAAxkBAAEFEPpirG-eZ4D0yOCaRsF55pQb9dc0BwACkhQAAhkLAAFImLEVRuflg-kkBA',
                'CAACAgIAAxkBAAEFEPtirG-en57o5PuzOx1IzIe8Ju7AdQACWgADSBeYL6UUWT302IJqJAQ',
                'CAACAgIAAxkBAAEFEPxirG-e8LXUgntNfB23pqNjh2JhGAACzhUAAv4qAAFI_0TEB4JUxBskBA',
                'CAACAgIAAxkBAAEFEP1irG-ePk40GokCabdqiExHftzOQwAC4yEAAgJF-Eu1njtvTHY6jSQE',
                'CAACAgIAAxkBAAEFEP5irG-emwbGqDbD6R3lbvzOJvYiogACfBYAAiJ9AAFIiSZ93-jQ9xwkBA',
                'CAACAgIAAxkBAAEFEP9irG-eR2rA4BzUn_Zhly2ZDYm5hwAC-hQAAjdbCUgXLsjAxh2AfCQE',
                'CAACAgQAAxkBAAEFEQABYqxvnjVn4wi00prOXGAj-0isNuUAAnIJAAK8LvlR5xknIhSsi9MkBA',
                'CAACAgQAAxkBAAEFEQFirG-em8ff903AESKcsklAAe6CUAAC6AsAAlRn-FF6SqAUoVqLFyQE',
                'CAACAgQAAxkBAAEFEQJirG-eK96EAvZREAp3tVeI_Do1qgAClQwAAnM56FEbOS3BEX99PSQE',
                'CAACAgQAAxkBAAEFEQNirG-ejURigrszonjReuvb_IkpoAACCgsAAiOK6VGMw_a6o5a3zCQE',
                'CAACAgQAAxkBAAEFEQRirG-eVB52_BrhVUjLDUNg1k-jmAAC3wsAAm148FJaOgGiiPTSoCQE',
                'CAACAgQAAxkBAAEFEQVirG-elSW8hpM-_pnqukgZRys5rgACAg4AAlMhsFK3xctzlXHzAyQE']


class CheckNumber(StatesGroup):
    check_number = State()


class DeleteAdvertisement(StatesGroup):
    delete = State()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot_commands.set_default_commands(dp=dp)
    if message.chat.type == 'private':
        db.delete_nul_advertisements()
        await bot.send_message(message.from_user.id, f"Приветствую, {message.from_user.full_name}",
                               reply_markup=nav2.menu())
    else:
        await message.reply("test")


@dp.message_handler(commands=['number'], state=None)
async def get_number(mes: types.Message):
    await bot.send_message(mes.from_user.id, 'Отправьте номер вашего заказа')
    await CheckNumber.check_number.set()


@dp.message_handler(commands=['random_sticker'])
async def send_random_sticker(mes: types.Message):
    await bot.send_sticker(mes.from_user.id, random.choice(sticker_list))


@dp.message_handler(commands=['voice'], state=None)
async def get_text_for_voice(mes: types.Message):
    await bot.send_message(mes.from_user.id, 'Отправьте текст для аудио')
    await ConvertStates.Convert.c1.set()

@dp.message_handler(commands=['convert_currency'])
async def get_mes_convert(mes: types.Message):
    await bot.send_message(mes.from_user.id, 'Отправьте значения в таком формате: "1 валюта, 2 валюта, количество"')


@dp.message_handler(content_types=['text'])
async def get_text(mes: types.Message):
    if mes.text == 'ПРОФИЛЬ':
        await bot.send_message(mes.from_user.id,
                           f'Количество ваших объявлений: {len(db.get_all_user_advertisements(mes.from_user.id))}',
                           reply_markup=nav2.main_keyboard())

    elif mes.text == 'ПОДПИСКА':
        if not db.get_sub_status(mes.from_user.id):
            await mes.delete()

            await bot.send_message(mes.from_user.id, 'Цена подписки 30 рублей. Выберите способ оплаты: ',
                                   reply_markup=nav.pay_menu())
            await Pay_sub.BuySubscribe.payment_choice.set()
        else:
            await bot.send_message(mes.from_user.id,
                                   f'У вас уже есть подписка\n! Заканчивается через {time_sub_day(db.get_time_sub(mes.from_user.id))}')

    else:
        try:
            convert_lst = mes.text.split(', ')
            time.sleep(1)
            await bot.send_message(mes.from_user.id,
                                   f"{convert_lst[2]} {convert_lst[0]} это {convert(convert_lst[0].upper(), convert_lst[1].upper(), convert_lst[2])} {convert_lst[1]}")
        except IndexError as e:
            pass


@dp.message_handler(content_types=['text'], state=ConvertStates.Convert.c1)
async def send_audio(mes: types.Message, state: FSMContext):
    text = mes.text
    my_audio = gTTS(text=text, lang='ru', slow=False)

    my_audio.save(f"voice_mes\\t_audio.mp3")
    time.sleep(2)

    file = open('voice_mes\\t_audio.mp3', 'rb')

    await bot.send_audio(mes.from_user.id, file)

    time.sleep(2)
    file.close()

    await state.finish()


# Отдел ЗАГС Адлерского района г. Сочи управления ЗАГС Краснодарского края
# ГУ МВД РОССИИ ПО КРАСНОДАРСКОМУ КРАЮ
# 79780078007
# elenakligman@yandex.ru
# 0322
# 033055
@dp.callback_query_handler(Text("add_advert"), state=None)
async def cm_start(call: types.CallbackQuery):
    if db.check_max_advertisements(call.from_user.id):
        db.set_advert_user_id(call.from_user.id)

        await bot.delete_message(call.from_user.id, call.message.message_id)
        await FSMAdmin.photo.set()

        db.set_advert_user_name(call.from_user.username, call.from_user.id)
        await bot.send_message(call.from_user.id, 'Загрузи фото', reply_markup=nav.Cancel_Menu)

    else:
        await call.message.reply('Можно отправить только 3 объявления')


@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message):
    try:
        db.set_photo(db.get_last_number(message.from_user.id), message.photo[0].file_id)

        await FSMAdmin.next()
        await message.reply('Теперь введи название', reply_markup=nav.Cancel_Menu)
    except IndexError:
        await message.reply(
            'Я не понимаю вас. Если вы хотите отменить загрузку и воспользоваться другой командой, нажмите ОТМЕНА')


@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message):
    db.set__advertisement_name(db.get_last_number(message.from_user.id), message.text)

    await FSMAdmin.next()
    await message.reply('Теперь введи описание', reply_markup=nav.Cancel_Menu)


@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message):
    db.set_description(db.get_last_number(message.from_user.id), message.text)

    await FSMAdmin.next()
    await message.reply('Теперь укажи цену', reply_markup=nav.Cancel_Menu)

    if '/' in message.text:
        await message.reply(
            'Если вы хотите отменить загрузку и воспользоваться другой командой, нажмите ОТМЕНА')


@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    db.set_price(db.get_last_number(message.from_user.id), float(message.text))

    await get_last_advertisement(message=message)

    time.sleep(2)
    await state.finish()


@dp.callback_query_handler(Text(startswith='cancel_'), state=FSMAdmin.all_states)
async def cancel_load(call: types.CallbackQuery, state: FSMContext):
    action = call.data.split('_')[1]
    if action == 'load':
        await state.finish()
        await call.message.reply('Вы отменили загрузку обьявления')
        db.delete_nul_advertisements()


@dp.callback_query_handler(Text("del_advert"))
async def delete_advert(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, 'Введите уникальный номер объявления перед удалением')
    await DeleteAdvertisement.delete.set()


@dp.message_handler(content_types=['text'], state=DeleteAdvertisement.delete)
async def check_delete(mes: types.Message, state: FSMContext):
    if db.check_user_number(mes.text, mes.from_user.id):
        db.delete_advertisement(mes.from_user.id, mes.text)
        await bot.send_message(mes.from_user.id, 'Объявление успешно удалено')
        await state.finish()
    else:
        await bot.send_message(mes.from_user.id, 'Объявление не найдено')
        await state.finish()

@dp.callback_query_handler(Text("user_advertisements"))
async def get_user_advertisements(call: types.CallbackQuery):
    await functions.advert_functions.get_user_advertisements(call=call)


@dp.callback_query_handler(Text(startswith='pay_'), state=Pay_sub.BuySubscribe.payment_choice)
async def choose_choice_of_payment(call: types.CallbackQuery, state: FSMContext):
    await functions.sub_functions.choose_choice_of_payment(call=call, state=state)


@dp.callback_query_handler(Text(contains="check"), state=Pay_sub.BuySubscribe.check_payment)
async def check(call: types.CallbackQuery, state: FSMContext):
    await functions.sub_functions.check(callback=call, state=state)


@dp.callback_query_handler(Text("watch_adverts"))
async def watch_adverts(call: types.CallbackQuery):
    await get_all_advertisements(call=call)

if __name__ == '__main__':
    executor.start_polling(dp)
