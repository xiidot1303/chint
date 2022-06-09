from django.http import HttpResponse, FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required

from django.db.models.functions import TruncDay
from django.db.models import Count
from django.contrib import messages

from datetime import datetime, timedelta
from app.models import *
from app.forms import *
from functions.get_object import *
from config import TELEGRAM_BOT_API_TOKEN
import telegram


@login_required
def laureate_list(request):
    laureates = Prizewinner.objects.all().order_by('-pk')
    context = {'list': laureates}
    return render(request, 'laureate/list_laureate.html', context)

@login_required
def laureate_change_status(request, pk, status):
    obj = Prizewinner.objects.get(pk=pk)
    about = About.objects.get(pk=1)
    user = obj.user

    # give point if cancelled request
    if status == 'cancel':
        user.point += obj.point
        user.save()

    if status != 'cancel' and obj.status == 'cancel':
        user.point -= obj.point
        if user.point < 0:
            messages.warning(request, 'У пользователя недостаточно баллов')
            return redirect(laureate_list)
        user.save()



    # send message to user by telegram
    bot = telegram.Bot(token=TELEGRAM_BOT_API_TOKEN)
    message = ''
    if status == 'conf' and obj.status != 'end':
        message += get_string('your prize is confirmed', user)
    elif status == 'cancel':
        message += get_string('your prize is cancelled', user).format(telegram_username = about.telegram_username, phone_number = about.phone1)
    elif status == 'wait':
        message += get_string('your prize is restored', user)
    if message:
        message += """\n<i>
        {text_prize}: {prize};
        {text_amount}: {amount};</i>
        """.format(
            text_prize = get_string('prize', user), prize = obj.prize.title,
            text_amount = get_string('amount', user), amount = obj.amount,
        )
    
        bot.sendMessage(chat_id = user.user_id, text=message, parse_mode = telegram.ParseMode.HTML)
    ####

    obj.status = status
    obj.save()
    return redirect(laureate_list)