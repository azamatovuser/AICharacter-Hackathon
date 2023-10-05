from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    button = InlineKeyboardMarkup()
    text = InlineKeyboardButton('Go to Web App', web_app=WebAppInfo(url='https://www.youtube.com'))
    button.add(text)
    await message.answer(f"Welcome to AICharacter bot, {message.from_user.full_name}!", reply_markup=button)