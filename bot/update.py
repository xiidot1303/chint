from telegram import Bot
from telegram.ext import Dispatcher, ConversationHandler, PicklePersistence
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from dotenv import load_dotenv
import os
from config import TELEGRAM_BOT_API_TOKEN, ENVIRONMENT
import requests

from bot import login, main, settings, get_points
from bot.conversationList import *
from bot.uz_ru import lang_dict



bot_obj = Bot(TELEGRAM_BOT_API_TOKEN)
persistence = PicklePersistence(filename='persistencebot')

if ENVIRONMENT != 'local': # in production
    updater = 1213
    dp = Dispatcher(bot_obj, None, workers=0, use_context=True, persistence=persistence)
else: # in local computer
    updater = Updater(token=TELEGRAM_BOT_API_TOKEN, use_context=True, persistence=persistence)
    dp = updater.dispatcher




login_handler = ConversationHandler(
    entry_points=[CommandHandler('start', main.start)],
    states = {
        SELECT_LANG: [MessageHandler(Filters.text(['UZ 🇺🇿', 'RU 🇷🇺']), login.select_lang)],
        SEND_NAME: [MessageHandler(Filters.text, login.send_name)],
        SEND_CONTACT: [MessageHandler(Filters.all, login.send_contact)],
    },
    fallbacks= [],
    name='login',
    persistent=True,
)



settings_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text(lang_dict['settings']), main.settings)],
    states = {
        ALL_SETTINGS: [MessageHandler(Filters.text, settings.all_settings)],
        LANG_SETTINGS: [CallbackQueryHandler(settings.lang_settings), CommandHandler('start', settings.lang_settings)],
        PHONE_SETTINGS: [MessageHandler(Filters.all, settings.phone_settings)],
        NAME_SETTINGS: [MessageHandler(Filters.text, settings.name_settings)],
    }, 
    fallbacks=[],
    name='settings',
    persistent=True,
)


get_points_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.text(lang_dict['get points']), main.get_points)],
    states = { 
        SELECT_PRODUCT: [MessageHandler(Filters.text, get_points.select_product)],
        CONFIRM_PRODUCT: [MessageHandler(Filters.text(lang_dict['next'] + lang_dict['back']), get_points.confirm_product)],
        SEND_AMOUNT: [MessageHandler(Filters.text, get_points.send_amount)],
        SEND_PHOTO: [MessageHandler(Filters.photo, get_points.send_photo), CommandHandler('start', get_points.send_photo),
            MessageHandler(Filters.text(lang_dict['back']), get_points.send_photo)],
        
    },
    fallbacks=[],
    name='get_points',
    persistent=True,
)


dp.add_handler(MessageHandler(Filters.text(lang_dict['my points']), main.my_points))
dp.add_handler(MessageHandler(Filters.text(lang_dict['info']), main.info))
dp.add_handler(MessageHandler(Filters.text(lang_dict['contact']), main.contact))

dp.add_handler(get_points_handler)
dp.add_handler(settings_handler)
dp.add_handler(login_handler)
