from app2.models import Request as Request2
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from bot.conversationList import *
from telegram.ext import ConversationHandler
from functions.bot import *
from functions.deco import *
from config import ENVIRONMENT

@is_start
def send_store_title(update, context):
    bot = context.bot
    answer = update.message.text

    Request2.objects.create(user = get_user_by_update(update), store = answer)

    update.message.reply_text(get_word('send photo_action2', update)) # button back is already sent
    try:
        if ENVIRONMENT == 'local':
            photo = 'AgACAgIAAxkBAAINGGKi9Zl-LVX9KXk8yJE3Lb_41-4uAAJ4vjEbVEoISUjmqYFe4iE0AQADAgADcwADJAQ'
        else:
            f = open('files/photos/b1.jpg', 'rb')
            photo = f
        reply_markup = ReplyKeyboardMarkup(keyboard=[[get_word('back', update)]], resize_keyboard=True)
        bot.send_photo(update.message.chat.id, photo = photo, reply_markup = reply_markup)
    except:
        a = 0
    return SEND_PHOTO_NEW


@is_start
def send_photo(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        Request2.objects.filter(user=get_user_by_update(update), status=None).delete()

        update.message.reply_text(get_word('type store title', update), 
            reply_markup = ReplyKeyboardMarkup(keyboard=[[get_word('main menu', update)]], resize_keyboard=True))
        return SEND_STORE_TITLE_NEW
    
    obj = Request2.objects.get(user = get_user_by_update(update), status=None)

    photo_id = bot.getFile(update.message.photo[-1].file_id)
    *args, file_name = str(photo_id.file_path).split('/')
    name, extension = file_name.split('.')
    random_file_name = generate_random_file_name()
    new_file_name = f"{random_file_name}.{extension}"
    d_photo = photo_id.download('files/photos/requests/{}'.format(new_file_name))
    obj.photo = str(d_photo).replace('files/', '')
    obj.save()
    
    update.message.reply_text(get_word('send photo2_action2', update)) # button back is already sent
    try:
        if ENVIRONMENT == 'local':
            photo = 'AgACAgIAAxkBAAINGWKi9dUAAasdOPYiE8wfSf7kzV9--wACer4xG1RKCEkSXrgJZkRtCgEAAwIAA3MAAyQE'
        else:
            f = open('files/photos/b2.jpg', 'rb')
            photo = f
        bot.send_photo(update.message.chat.id, photo = photo)
    except:
        a = 0
    return SEND_PHOTO2_NEW

@is_start
def send_photo2(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        update.message.reply_text(get_word('send photo_action2', update))
        if ENVIRONMENT == 'local':
            photo = 'AgACAgIAAxkBAAINGGKi9Zl-LVX9KXk8yJE3Lb_41-4uAAJ4vjEbVEoISUjmqYFe4iE0AQADAgADcwADJAQ'
        else:
            f = open('files/photos/b1.jpg', 'rb')
            photo = f
        bot.send_photo(update.message.chat.id, photo = photo)
        return SEND_PHOTO_NEW
    
    obj = Request2.objects.get(user = get_user_by_update(update), status=None)

    photo_id = bot.getFile(update.message.photo[-1].file_id)
    *args, file_name = str(photo_id.file_path).split('/')
    name, extension = file_name.split('.')
    random_file_name = generate_random_file_name()
    new_file_name = f"{random_file_name}.{extension}"
    d_photo = photo_id.download('files/photos/requests/{}'.format(new_file_name))
    obj.photo2 = str(d_photo).replace('files/', '')
    obj.save()

    update.message.reply_text(get_word('send photo3_action2', update)) # button back is already sent
    try:
        if ENVIRONMENT == 'local':
            photo = 'AgACAgIAAxkBAAINGWKi9dUAAasdOPYiE8wfSf7kzV9--wACer4xG1RKCEkSXrgJZkRtCgEAAwIAA3MAAyQE'
        else:
            f = open('files/photos/b3.png', 'rb')
            photo = f
        bot.send_photo(update.message.chat.id, photo = photo)
    except:
        a = 0
    return SEND_PHOTO3_NEW


@is_start
def send_photo3(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        update.message.reply_text(get_word('send photo2_action2', update))
        if ENVIRONMENT == 'local':
            photo = 'AgACAgIAAxkBAAINGGKi9Zl-LVX9KXk8yJE3Lb_41-4uAAJ4vjEbVEoISUjmqYFe4iE0AQADAgADcwADJAQ'
        else:
            f = open('files/photos/b2.jpg', 'rb')
            photo = f
        bot.send_photo(update.message.chat.id, photo = photo)
        return SEND_PHOTO2_NEW
    
    obj = Request2.objects.get(user = get_user_by_update(update), status=None)
    photo_id = bot.getFile(update.message.photo[-1].file_id)
    *args, file_name = str(photo_id.file_path).split('/')
    name, extension = file_name.split('.')
    random_file_name = generate_random_file_name()
    new_file_name = f"{random_file_name}.{extension}"
    d_photo = photo_id.download('files/photos/requests/{}'.format(new_file_name))
    obj.photo3 = str(d_photo).replace('files/', '')
    obj.save()


    update.message.reply_text(get_word('completed request', update))
    obj.status = 'wait'
    obj.date = datetime.now()
    obj.save()
    main_menu(update,context)
    return ConversationHandler.END