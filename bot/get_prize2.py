from app2.models import *
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from bot.conversationList import *
from telegram.ext import ConversationHandler
from functions.bot import *
from functions.deco import *


@is_start
def select_prize(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        main_menu(update, context)
        return ConversationHandler.END
    user = get_user_by_update(update)
    if user.lang == 'uz':
        prize = Prize.objects.filter(title_uz = answer)[0]
        title = prize.title_uz
        description = prize.description_uz
    else: # ru
        prize = Prize.objects.filter(title = answer)[0]
        title = prize.title
        description = prize.description

    caption = '⚫️ {word_title}: {title};\n⚫️ {word_point}: {point};\n\n💬  {description};'.format(
        word_title=get_word('title', update), title = title, word_point=get_word('point', update), 
            point=prize.point, description = description
    )
    if prize.photo:
        bot.send_photo(update.message.chat.id, photo = prize.photo, 
            caption = caption, reply_markup = ReplyKeyboardMarkup(keyboard=[[get_word('next', update)], [get_word('back', update)]], resize_keyboard=True))
    else:
        bot.send_message(update.message.chat.id, caption, reply_markup = ReplyKeyboardMarkup(
            keyboard=[[get_word('next', update)], [get_word('back', update)]], resize_keyboard=True))

    Prizewinner.objects.create(user = get_user_by_update(update), prize = prize)

    return CONFIRM_PRIZE


@is_start
def confirm_prize(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        obj = Prizewinner.objects.get(user=get_user_by_update(update), status=None)
        obj.delete()
        make_button_prizes(update, context)
        return SELECT_PRIZE
    
    if answer == get_word('next', update):
        update.message.reply_text(get_word('type amount', update), 
            reply_markup = ReplyKeyboardMarkup(keyboard=[[get_word('back', update)]], resize_keyboard=True))
        return SEND_AMOUNT_PRIZE

@is_start
def send_amount_prize(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        obj = Prizewinner.objects.get(user=get_user_by_update(update), status = None)
        user = get_user_by_update(update)
        if user.lang == 'uz':
            update.message.text = obj.prize.title_uz
        else: # ru
            update.message.text = obj.prize.title

        obj.delete()
        select_prize(update, context)
        return CONFIRM_PRIZE
    
    obj = Prizewinner.objects.get(user = get_user_by_update(update), status=None)
    
    try:
        
        obj.amount = float(answer)
        obj.point = float(answer) * float(obj.prize.point)
        
        # check that user have points or not
        user = get_user_by_update(update)
        
        if (user.point2 - obj.point) < 0:
            update.message.reply_text('{}\n{}: {}'.format(
                get_word('not enough points', update), get_word('your points', update), user.point2
            ))
            return

        obj.save()
    except:
        update.message.reply_text('{}\n{}'.format(get_word('incorrect value', update), get_word('type amount of products', update)))
        return
    
    update.message.reply_text(get_word('are sure exchange points', update), reply_markup = 
        ReplyKeyboardMarkup(keyboard=[[get_word('yes', update), get_word('no', update)], [get_word('back', update)]], resize_keyboard=True))

    return CONFIRM_EXCHANGE


@is_start
def confirm_exchange(update, context):
    bot = context.bot
    answer = update.message.text

    if answer == get_word('back', update):
        update.message.reply_text(get_word('type amount of products', update), 
            reply_markup = ReplyKeyboardMarkup(keyboard=[[get_word('back', update)]], resize_keyboard=True))
        return SEND_AMOUNT_PRIZE    
    
    obj = Prizewinner.objects.get(user = get_user_by_update(update), status=None)
    user = get_user_by_update(update)
    if answer == get_word('yes', update):
        update.message.reply_text(get_word('completed getting prize', update))
        user.point2 -= obj.point
        user.save()
        obj.status = 'wait'
        obj.save()

    elif answer == get_word('no', update):
        obj.delete()
    
    main_menu(update,context)
    return ConversationHandler.END
