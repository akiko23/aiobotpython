from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("load", "Загрузить объявление"),
        types.BotCommand("voice", "Ввод и отправка голосового сообщения"),
        types.BotCommand("convert_currency", "Конвертация валют"),
    ])
