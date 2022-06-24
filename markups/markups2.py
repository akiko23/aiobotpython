from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

btnProfile = InlineKeyboardButton('НАШЕ РАСПОЛОЖЕНИЕ',
                                  url='https://www.google.com/maps/place/%D0%94%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9+%D1%81%D0%B0%D0%B4+zxcursed/@43.402812,39.9791471,19.5z/data=!4m14!1m8!3m7!1s0x40f595ea29f7e983:0xf6215fe253ebfb13!2z0JTQtdGC0YHQutC40Lkg0YHQsNC0IHp4Y3Vyc2Vk!8m2!3d43.4029005!4d39.9793476!9m1!1b1!3m4!1s0x40f595ea29f7e983:0xf6215fe253ebfb13!8m2!3d43.4029005!4d39.9793476?hl=ru')
reply = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
reply.add(btnProfile)

btnToCancel = InlineKeyboardButton(text="ОТМЕНА", callback_data='cancel_load')

Cancel_Menu = InlineKeyboardMarkup(row_width=1)
Cancel_Menu.insert(btnToCancel)

"""valutes_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('USD'),
            KeyboardButton('UAH'),
            KeyboardButton('SUM'),
        ]
    ],

    resize_keyboard=True, row_width=2
)

admin_markup = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton('РЕКЛАМА'),
            KeyboardButton('БАН')
        ]
    ],
    resize_keyboard=True,
    row_width=2

)


def get_keyboard():
    # Генерация клавиатуры.
    buttons = [
        InlineKeyboardButton(text="-1", callback_data="num_decr"),
        InlineKeyboardButton(text="+1", callback_data="num_incr"),
        InlineKeyboardButton(text="+10000", callback_data="num_incr10000"),
        InlineKeyboardButton(text="+100000", callback_data="num_incr100000"),
        InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def admin_panel():
    buttons = [
        InlineKeyboardButton(text='РЕКЛАМА', callback_data='adm_advertising'),
        InlineKeyboardButton(text='БАН', callback_data='adm_ban')
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


btnTopUp = InlineKeyboardButton(text="🏦 Пополнить баланс", callback_data='top_up')

topUpMenu = InlineKeyboardMarkup(row_width=1)
topUpMenu.insert(btnTopUp)


def buy_menu(isurl=True, url="", bill=""):
    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if isurl:
        btn_UrlQiwi = InlineKeyboardButton(text="Ссылка на оплату", url=url)
        qiwiMenu.insert(btn_UrlQiwi)

    btn_checkQiwi = InlineKeyboardButton(text="Проверить оплату", callback_data="check_" + bill)
    btn_cancel = InlineKeyboardButton(text="Отмена", callback_data="cancel")
    qiwiMenu.add(btn_checkQiwi, btn_cancel)
    return qiwiMenu


def admin_panel_advertising():
    buttons = [
        InlineKeyboardButton(text='Канал1', callback_data='advertising_chanel1'),
        InlineKeyboardButton(text='Канал2', callback_data='advertising_chanel2'),
        InlineKeyboardButton(text='Все каналы', callback_data='advertising_all'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def send_advertising_again():
    buttons = [
        InlineKeyboardButton(text='Отправить еще раз', callback_data='adm_advertising'),
        InlineKeyboardButton(text='Отмена', callback_data='cancel_after'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard"""

def pay_menu():
    buttons = [
        InlineKeyboardButton(text='QIWI', callback_data='pay_qiwi'),
        InlineKeyboardButton(text='Сбербанк', callback_data='pay_sber'),
        InlineKeyboardButton(text='U-money', callback_data='pay_umoney'),
        InlineKeyboardButton(text='ОТМЕНА', callback_data='pay_cancel')
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard

def pay_subscribe_by_balance():
    buttons = [
        InlineKeyboardButton(text='Да', callback_data='buy_sub_by_balance'),
        InlineKeyboardButton(text='Нет, купить на прямую', callback_data='buy_sub_by_other_bank')
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard
