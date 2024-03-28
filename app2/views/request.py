from django.http import HttpResponse, FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required

from django.db.models.functions import TruncDay
from django.db.models import Count

from datetime import datetime, timedelta
from app2.models import *
from app2.forms import *
from functions.get_object import *
from config import TELEGRAM_BOT_API_TOKEN
import telegram


@login_required
def request_list(request):
    requests = Request.objects.filter(status='wait').order_by('-pk')
    context = {'list': requests}
    return render(request, 'app2/request/list_request.html', context)

@login_required
def request_change_status(request, pk, status):
    obj = Request.objects.get(pk=pk)
    about = About.objects.get(pk=1)
    user = obj.user
    point = 0
    if status == 'wait' and obj.status == 'conf':
        user.point -= obj.point
        point = '{} {}'.format(str(0 - obj.point), '⬇️')
    elif status == 'conf' and obj.status == 'wait':
        user.point += obj.point
        point = '{} {}'.format(obj.point, '⬆️')
    user.save()
    obj.status = status
    obj.save()

    # send message to user by telegram
    bot = telegram.Bot(token=TELEGRAM_BOT_API_TOKEN)
    message = ''
    if status == 'conf':
        message += get_string('your request is confirmed', user)
    elif status == 'cancel':
        message += get_string('your request is cancelled', user).format(telegram_username = about.telegram_username, phone_number = about.phone1)
    elif status == 'wait':
        message += get_string('your request is restored', user)

    message += """\n<i>
    {text_product}: {product};
    {text_amount}: {amount};</i>
    <b>{text_point}: {point};</b>
    """.format(
        text_product = get_string('product', user), product = obj.product.title,
        text_amount = get_string('amount', user), amount = obj.amount,
        text_point = get_string('point', user), point = point,
    )

    bot.sendMessage(chat_id = user.user_id, text=message, parse_mode = telegram.ParseMode.HTML)
    #####

    return redirect(request_list)
