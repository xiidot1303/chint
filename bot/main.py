from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ConversationHandler

from app.models import *
from app2.models import About as About2, Rule as Rule2
from bot.conversationList import SELECT_LANG, ALL_SETTINGS
from functions.bot import *
from django.db.models import Sum, F
import config

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
    con = get_condition_by_update(update)
    if con == 1:
        make_button_products(update, context)
        return SELECT_PRODUCT
    elif con == 2:
        markup = ReplyKeyboardMarkup([[get_word('main menu', update)]], resize_keyboard=True)
        update.message.reply_text(get_word('type store title', update), reply_markup = markup)
        return SEND_STORE_TITLE_NEW

def get_prizes(update, context):
    con = get_condition_by_update(update)
    if con == 1:
        make_button_prizes(update, context)
        return SELECT_PRIZE
    elif con == 2:
        make_button_prizes2(update, context)
        return SELECT_PRIZE_NEW


def info(update, context):
    bot = context.bot
    con = get_condition_by_update(update)
    if con == 1:
        obj = About.objects.get(pk=1)
    elif con == 2:
        obj = About2.objects.get(pk=1)

    # *args, file_type = str(obj.file).split('.')
    user = get_user_by_update(update)
    if user.lang == 'uz':
        file = open('files/{}'.format(str(obj.file_uz)), 'rb')
    else:
        file = open('files/{}'.format(str(obj.file_ru)), 'rb')

    try:
        try:
            bot.send_photo(update.message.chat.id, file)
        except:
            bot.send_video(update.message.chat.id, file)
    except:
        bot.send_document(update.message.chat.id, file)

    # if file_type == 'xls' or file_type == 'xlsx':
    #     bot.send_document(update.message.chat.id, file)
    # else:
    #     bot.send_photo(update.message.chat.id, file)

    # update.message.reply_text(obj.action)


def rule(update, context):
    bot = context.bot
    con = get_condition_by_update(update)
    if con == 1:
        obj = Rule.objects.get(pk=1)
    elif con == 2:
        obj = Rule2.objects.get(pk=1)

    user = get_user_by_update(update)
    file = None
    if user.lang == 'uz':
        if obj.file_uz:
            # file = open('files/{}'.format(str(obj.file_uz)), 'rb')
            file = 'BQACAgQAAxkBAAIfJ2OAVvtDSwp2X58pBd6uJHruddmEAAIFEgACMT4IUJEAAZhNLylsbisE'
        text = obj.text_uz
    else:
        if obj.file_ru:
            # file = open('files/{}'.format(str(obj.file_ru)), 'rb')
            file = 'BQACAgQAAxkBAAIfKWOAVzKuBFGENgsfzTiJ7uy0TTmFAAIHEgACMT4IUGsNCkggeCbyKwQ'
        text = obj.text_ru
    try:
        try:
            bot.send_photo(update.message.chat.id, file)
        except:
            bot.send_video(update.message.chat.id, file)
    except:
        if file:
            bot.send_document(update.message.chat.id, file)

    bot.send_message(update.message.chat.id, text)


def contact(update, context):   
    con = get_condition_by_update(update)
    if con == 1:
        obj = About.objects.get(pk=1)
    elif con == 2:
        obj = About2.objects.get(pk=1)

    user = get_user_by_update(update)
    if user.lang == 'uz':
        update.message.reply_text(obj.contact_uz, parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        update.message.reply_text(obj.contact_ru, parse_mode=telegram.ParseMode.MARKDOWN)
        

def my_points(update, context):
    user = get_user_by_update(update)
    con = get_condition_by_update(update)
    user_point = user.point if con == 1 else user.point2
    # points = Request.objects.filter(user = user).values('user__name').annotate(p=Sum(F('point')*F('amount')))[0]['p']
    msg = '<b>{}</b>: {}'.format(get_word('your points', update), user_point)
    # msg += '\n\n👉 <a href="{}/statistic">🔗{}</a> 👈'.format(config.URL, get_word('action results', update))
    msg += '\n\n👉 <a href="{}">🔗{}</a> 👈'.format(config.URL, get_word('action results', update))
    i_top20 = InlineKeyboardButton(text=get_word('top20', update), callback_data='top20')
    update.message.reply_text(msg, reply_markup = InlineKeyboardMarkup([[i_top20]]), parse_mode = telegram.ParseMode.HTML)

def top20(update, context):
    bot = context.bot
    update = update.callback_query
    con = get_condition_by_update(update)
    if update.data == 'top20':
        current_user  = get_user_by_update(update)

        # query_users = Bot_user.objects.all().annotate(total=F('point')).order_by('-total')
        if con == 1:
            query_users = Bot_user.objects.all().exclude(phone=None).order_by('-total')
        else:
            query_users = Bot_user.objects.all().exclude(phone=None).order_by('-total2')
        list_users = list(query_users.values_list('pk', flat=True))
        top20_list = query_users[:20]
        user_index = list_users.index(current_user.pk) + 1
    
        message = '⬆️ Top 20:\n\n'
        n = 1
        for user in top20_list:
            text = ''
            if n == 1:
                text += '1️⃣. '
            elif n == 2:
                text += '2️⃣. '
            elif n == 3:
                text += '3️⃣. '
            else:
                text += '{}. '.format(n)
            user_total = user.total if con == 1 else user.total2
            text += '{}, {}, {};\n'.format(user.name, user.city, user_total)
            if user == current_user:
                text = '<u><b>{}</b></u>'.format(text)
            message += text
            n += 1
    
        if user_index > 20:
            if user_index != 21:
                message += '....\n'
            current_user_total = current_user.total if con == 1 else current_user.total2
            message += '{}. {}, {}, {};'.format(user_index, current_user.name, current_user.city, current_user_total)
        
        update.message.reply_text(message, parse_mode = telegram.ParseMode.HTML)

    

def nura_store(update, context):
    pass