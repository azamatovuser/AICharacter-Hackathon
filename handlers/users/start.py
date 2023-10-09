from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(KeyboardButton('Go to Web App', web_app=WebAppInfo(url='https://webapp-tau-beige.vercel.app')))
    await message.answer(f"Welcome to AICharacter bot, {message.from_user.full_name}!", reply_markup=button)