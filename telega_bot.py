from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from MyToken import token
from telebot import types
import telebot

bot = telebot.TeleBot(token)

entry = {}
inline_keyboard = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('продолжить', callback_data='first')
inline_keyboard.add(btn1)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет, этот бот может предоставить вам информацию о разных грантах,'
                              ' инвестициях и стажировках, а так же содержит в кнопке "чаво" ответы на частые вопросы', reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'first':
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        k1 = types.KeyboardButton('Гранты')
        k2 = types.KeyboardButton('Инвестиции')
        k3 = types.KeyboardButton('Поддержка')
        k4 = types.KeyboardButton('ЧаВо')
        income_keyboard.add(k1, k2, k3, k4)
        msg = bot.send_message(chat_id, 'Выбери кнопку', reply_markup=income_keyboard)



bot.polling()

