import time

import aiogram.utils.exceptions
import markups.markups as nav

from aiogram import types

from config import *


async def get_user_advertisements(call: types.CallbackQuery):
    user_advertisements = []

    try:
        if len(db.get_all_user_advertisements(call.from_user.id)) > 0:
            for advertisement_crt in db.get_all_user_advertisements(call.from_user.id):
                for element in advertisement_crt:
                    user_advertisements.append(str(element))

            for i in range(len(user_advertisements)):
                if i == 0 or i % 5 == 0:
                    user_photo = user_advertisements[i]
                    ad_name = user_advertisements[i + 1]
                    ad_description = user_advertisements[i + 2]
                    ad_price = user_advertisements[i + 3]
                    ad_number = user_advertisements[i + 4]

                    await bot.send_photo(call.from_user.id, user_photo,
                                         caption=f"Уникальный номер: {ad_number}\nНазвание: {ad_name} \nОписание: {ad_description} \nЦена: {ad_price}",
                                         reply_markup=nav.delete_advert())
                    time.sleep(1)
        else:
            await bot.send_message(call.from_user.id, 'У вас нет объявлений')

    except aiogram.utils.exceptions.BadRequest as e:
        await bot.send_message(call.from_user.id, 'У вас нет объявлений')


async def get_last_advertisement(message: types.Message):
    result = db.get_all_user_advertisements(message.from_user.id)[-1]

    photo_id = result[0]
    name = result[1]
    description = result[2]
    price = result[3]
    number = result[4]


    await bot.send_photo(message.from_user.id, photo=photo_id,
                         caption=f"Уникальный номер: {number}\nНазвание: {name} \nОписание: {description} \nЦена: {price}")


async def get_all_advertisements(call: types.CallbackQuery):
    user_advertisements = []

    try:
        if len(db.get_all_advertisements(call.from_user.id)) > 0:
            for advertisement_crt in db.get_all_advertisements(call.from_user.id):
                for element in advertisement_crt:
                    user_advertisements.append(str(element))

            try:
                for ad in user_advertisements:
                    for i in range(len(ad)):
                        if i == 0 or i % 5 == 0:
                            user_photo = user_advertisements[i]
                            ad_name = user_advertisements[i + 1]
                            ad_description = user_advertisements[i + 2]
                            ad_price = user_advertisements[i + 3]
                            user_name = user_advertisements[i + 4]

                            await bot.send_photo(call.from_user.id, user_photo,
                                                 caption=f"Название: {ad_name} \nОписание: {ad_description} \nЦена: {ad_price}\nПисать сюда: @{user_name}")
                            time.sleep(1)
            except IndexError as e:
                pass
        else:
            await bot.send_message(call.from_user.id, 'Нет объявлений')

    except aiogram.utils.exceptions.BadRequest as e:
        pass
