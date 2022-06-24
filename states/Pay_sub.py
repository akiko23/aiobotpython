from aiogram.dispatcher.filters.state import StatesGroup, State

class BuySubscribe(StatesGroup):
    payment_choice = State()
    check_payment = State()
