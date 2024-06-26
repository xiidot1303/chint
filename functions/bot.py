from telegram import ReplyKeyboardMarkup, KeyboardButton
import telegram
from bot.uz_ru import lang_dict
from app.models import *
from app2.models import Prize as Prize2
from telegram.ext import ConversationHandler
from datetime import date, datetime
from bot.conversationList import *
import random
import string

def main_menu(update, context):
    try:
        a = update.callback_query.id
        update = update.callback_query
    except:
        www= 0 # do nothing
    
    bot = context.bot
    keyboard=[
            [get_word('get points', update), get_word('my points', update)], 
            [get_word('get prizes', update), get_word('contact', update)], 
            [get_word('settings', update), get_word('rules', update)],
            [get_word('info', update)], 
        ]
    bot.send_message(update.message.chat.id, get_word('main menu', update), reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))
    check_username(update)

    
def make_button_settings(update, context):
    try:
        a = update.callback_query.id
        update = update.callback_query
    except:
        www= 0 # do nothing
    bot = context.bot
    keyboard=[[get_word('change lang', update)], [get_word('change name', update)], [get_word('change phone number', update)], [get_word('main menu', update)]]
    bot.send_message(update.message.chat.id, get_word('settings desc', update), reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))




def make_button_products(update, context):
    bot = context.bot
    keyboards = list(Product.objects.all().values_list('title'))
    keyboards.append([get_word('back', update)])
    bot.send_message(update.message.chat.id, get_word('select products', update), reply_markup = ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True))

def make_button_prizes(update, context):
    bot = context.bot
    user = get_user_by_update(update)
    if user.lang == 'uz':
        keyboards = list(Prize.objects.all().values_list('title_uz'))
    else: #ru
        keyboards = list(Prize.objects.all().values_list('title'))
         
    keyboards.append([get_word('back', update)])
    bot.send_message(update.message.chat.id, get_word('select products', update), reply_markup = ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True))

def make_button_prizes2(update, context):
    bot = context.bot
    user = get_user_by_update(update)
    if user.lang == 'uz':
        keyboards = list(Prize2.objects.all().values_list('title_uz'))
    else: #ru
        keyboards = list(Prize2.objects.all().values_list('title'))
         
    keyboards.append([get_word('back', update)])
    bot.send_message(update.message.chat.id, get_word('select products', update), reply_markup = ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True))




def get_word(text, update):
    user = Bot_user.objects.get(user_id=update.message.chat.id)
    if user.lang == 'uz':
        return lang_dict[text][0]
    else:
       return lang_dict[text][1]

def is_registered(id):
    if Bot_user.objects.filter(user_id=id):
        return True
    else:
        return False

def get_user_by_update(update):
    user = Bot_user.objects.get(user_id=update.message.chat.id)
    return user

def check_username(update):
    user = get_user_by_update(update)
    
    if user.username != update.message.chat.username:
        user.username = update.message.chat.username
        user.save()
    if user.firstname != update.message.chat.first_name:
        user.firstname = update.message.chat.first_name
        user.save()

def get_condition_by_update(update):
    user = get_user_by_update(update)
    return user.condition

def generate_random_file_name(length = 12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))