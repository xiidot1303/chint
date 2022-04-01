from django.http import HttpResponse, FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from telegram import Update
from bot.update import dp, updater
from dotenv import load_dotenv
import os
import json
from django.views.decorators.csrf import csrf_exempt
from config import TELEGRAM_BOT_API_TOKEN, ENVIRONMENT


@csrf_exempt
def bot_webhook(request):

    if ENVIRONMENT == 'local':
        updater.start_polling()
    else:
        update = Update.de_json(json.loads(request.body.decode('utf-8')), dp.bot)
        dp.process_update(update)
    return HttpResponse('Bot started!')

