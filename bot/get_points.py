from app.models import *
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from bot.conversationList import *
from telegram.ext import ConversationHandler
from functions.bot import *
from functions.deco import *

@is_start
def select_product(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        main_menu(update, context)
        return ConversationHandler.END

    product = Product.objects.filter(title = answer)[0]
    caption = '⚫️ {word_title}: {title};\n⚫️ {word_point}: {point};\n\n💬  {description};'.format(
        word_title=get_word('title', update), title = product.title, word_point=get_word('point', update), 
            point=product.point, description = product.description
    )
    if product.photo:
        bot.send_photo(update.message.chat.id, photo = product.photo, 
            caption = caption, reply_markup = ReplyKeyboardMarkup(keyboard=[[get_word('next', update)], [get_word('back', update)]], resize_keyboard=True))
    else:
        bot.send_message(update.message.chat.id, caption, reply_markup = ReplyKeyboardMarkup(
            keyboard=[[get_word('next', update)], [get_word('back', update)]], resize_keyboard=True))

    Request.objects.create(user = get_user_by_update(update), product = product)

    return CONFIRM_PRODUCT


@is_start
def confirm_product(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        obj = Request.objects.get(user=get_user_by_update(update), status=None)
        obj.delete()
        make_button_products(update, context)
        return SELECT_PRODUCT
    
    if answer == get_word('next', update):
        update.message.reply_text(get_word('type amount of products', update), 
            reply_markup = ReplyKeyboardMarkup(keyboard=[[get_word('back', update)]], resize_keyboard=True))
        return SEND_AMOUNT

@is_start
def send_amount(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        obj = Request.objects.get(user=get_user_by_update(update), status = None)
        update.message.text = obj.product.title
        obj.delete()
        select_product(update, context)
        return CONFIRM_PRODUCT
    
    obj = Request.objects.get(user = get_user_by_update(update), status=None)
    try:
        obj.amount = float(answer)
        obj.point = float(answer) * float(obj.product.point)
        obj.save()
    except:
        update.message.reply_text('{}\n{}'.format(get_word('incorrect value', update), get_word('type amount of products', update)))
        return
    
    update.message.reply_text(get_word('send photo', update)) # button back is already sent
    try:
        bot.send_photo(update.message.chat.id, photo = 'AgACAgIAAxkBAAINGGKi9Zl-LVX9KXk8yJE3Lb_41-4uAAJ4vjEbVEoISUjmqYFe4iE0AQADAgADcwADJAQ')
    except:
        a = 0
    return SEND_PHOTO


@is_start
def send_photo(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        update.message.reply_text(get_word('type amount of products', update), 
            reply_markup = ReplyKeyboardMarkup(keyboard=[[get_word('back', update)]], resize_keyboard=True))
        return SEND_AMOUNT
    
    obj = Request.objects.get(user = get_user_by_update(update), status=None)

    photo_id = bot.getFile(update.message.photo[-1].file_id)
    *args, file_name = str(photo_id.file_path).split('/')
    d_photo = photo_id.download('files/photos/requests/{}'.format(file_name))
    obj.photo = str(d_photo).replace('files/', '')
    obj.save()
    
    update.message.reply_text(get_word('send photo2', update)) # button back is already sent
    try:
        bot.send_photo(update.message.chat.id, photo = 'AgACAgIAAxkBAAINGWKi9dUAAasdOPYiE8wfSf7kzV9--wACer4xG1RKCEkSXrgJZkRtCgEAAwIAA3MAAyQE')
    except:
        a = 0
    return SEND_PHOTO2

@is_start
def send_photo2(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        update.message.reply_text(get_word('send photo', update))
        return SEND_PHOTO
    
    obj = Request.objects.get(user = get_user_by_update(update), status=None)

    photo_id = bot.getFile(update.message.photo[-1].file_id)
    *args, file_name = str(photo_id.file_path).split('/')
    d_photo = photo_id.download('files/photos/requests/{}'.format(file_name))
    obj.photo2 = str(d_photo).replace('files/', '')
    obj.save()
    
    update.message.reply_text(get_word('completed request', update))
    obj.status = 'wait'
    obj.save()
    main_menu(update,context)
    return ConversationHandler.END