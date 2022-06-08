from app.models import *
from bot.uz_ru import lang_dict

def get_string(text, user):
    if user.lang == 'uz':
        return lang_dict[text][0]
    else:
       return lang_dict[text][1]