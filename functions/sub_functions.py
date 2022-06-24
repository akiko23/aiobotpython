import datetime
import random
import time

import markups.markups2 as nav

from aiogram import types
from aiogram.dispatcher import FSMContext

from config import *
from states import Pay_sub



def time_sub_day(get_time):
    time_now = int(time.time())
    middle_time = int(get_time) - time_now

    if middle_time <= 0:
        return False
    else:
        dt = str(datetime.timedelta(seconds=middle_time))
        return dt

def days_to_seconds(days):
    return days * 60 * 60 * 24

async def check(callback: types.CallbackQuery, state: FSMContext):
    bill = str(callback.data[6:])
    info = db.get_check(bill)

    action = callback.data.split('_')[1]

    if action == 'cancel':
        await bot.send_message(callback.from_user.id, 'Оплата отменена')
        await state.finish()

    if info:
        if str(p2p.check(bill_id=bill).status) == "PAID":
            time_sub = int(time.time()) + days_to_seconds(31)

            await bot.send_message(callback.from_user.id,
                                   f'Подписка оформлена. Она еще будет действовать 30 дней')

            db.set_time_sub(callback.from_user.id, time_sub)
            db.set_sub_status(callback.from_user.id, 'paid')
            await state.finish()

        else:
            await bot.send_message(callback.from_user.id, 'Вы не оплатили счет :(',
                                   reply_markup=nav.buy_menu(False, bill=bill))
    else:
        await bot.send_message(callback.from_user.id, 'Счет не найден :(')


async def choose_choice_of_payment(call: types.CallbackQuery, state: FSMContext):
    action = call.data.split('_')[1]

    if action == 'qiwi':
        message_money = 30

        comment = str(call.from_user.id) + "_" + str(random.randint(1000, 9999))
        bill = p2p.bill(amount=message_money, lifetime=15, comment=comment)

        db.add_check(call.from_user.id, message_money, bill.bill_id)
        url = bill.pay_url

        await bot.send_message(call.from_user.id,
                               f"Вам нужно отправить {message_money} рублей на наш счет киви\nСсылка: {url}\nКомментарий к оплате:{comment}",
                               reply_markup=nav.buy_menu(url=bill.pay_url, bill=bill.bill_id))
        await Pay_sub.BuySubscribe.check_payment.set()

    elif action == 'cancel':
        await bot.send_message(call.from_user.id, 'Оплата отменена')
        await state.finish()