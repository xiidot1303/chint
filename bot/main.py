from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ConversationHandler

from app.models import *
from bot.conversationList import SELECT_LANG, ALL_SETTINGS
from functions.bot import *

def start(update, context):
    
    if is_registered(update.message.chat.id):
        main_menu(update, context)
    else:
        hello_text = '🤖 Xush kelibsiz!\n Bot tilini tanlang  🌎 \n\n ➖➖➖➖➖➖➖➖➖➖➖➖\n\n 👋 Добро пожаловать \n \U0001F1FA\U0001F1FF Выберите язык бота \U0001F1F7\U0001F1FA'
        update.message.reply_text(hello_text, reply_markup=ReplyKeyboardMarkup(keyboard=[['UZ 🇺🇿', 'RU 🇷🇺']], resize_keyboard=True))
        return SELECT_LANG

def settings(update, context):
    make_button_settings(update, context)
    return ALL_SETTINGS

def get_points(update, context):
    
    make_button_products(update, context)
    return SELECT_PRODUCT

def info(update, context):
    bot = context.bot
    obj = About.objects.get(pk=1)
    file = open('files/{}'.format(str(obj.file)), 'rb')
    bot.send_document(update.message.chat.id, file)
    # update.message.reply_text(obj.action)

def contact(update, context):   
    obj = About.objects.get(pk=1)
    update.message.reply_text(obj.contact)