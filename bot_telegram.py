from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import emoji
import keyboards as kb
import os

country = ['ru','kz','fr','by','es','nl'], [':Russia:','Kazakhstan',':France:',':Belarus:',':Spain:',':Netherlands:']

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,"Привет!\nОткуда ты?", reply_markup=kb.kb_choiсe_country)

@dp.callback_query_handler(lambda c: True)
async def process_callback_button(call):
    await bot.answer_callback_query(callback_query_id=call.id)
    for i in range(len(country[0])):
        if country[0][i] == call.data:
            kb.create_button(country[0][i])
            await bot.send_message(call.from_user.id, emoji.emojize("Ты выбрал " + country[1][i]), reply_markup=kb.inline_keyboard_sites)

executor.start_polling(dp, skip_updates=True)