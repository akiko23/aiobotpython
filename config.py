from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyqiwip2p import QiwiP2P

from db import Database

BOT_TOKEN = '5418428043:AAEWqhzqka8Hs9JihfrM5yrIySeVaR9Ae4U'
UKASSA_TOKEN = '381764678:TEST:38844'


bot = Bot(BOT_TOKEN)
p2p = QiwiP2P(auth_key='eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InNzczVvMC0wMCIsInVzZXJfaWQiOiI3OTg5NzUwNTg2MCIsInNlY3JldCI6ImMwYTNhODc5ZDQxMTE5OGZmMDJkYjQzZjE0MTA5YWU5ZDYzZTZjN2MwYWYzZjc1ZDZiNGExODg0YTVjNGM3NjcifX0=')

dp = Dispatcher(bot, storage=MemoryStorage())

db = Database("C:\\Users\\hdhrh\\Desktop\\pythonProject\\database.db")