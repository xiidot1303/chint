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
from django.db.models import Count, Sum, F, Q
import pandas as pd


@login_required
def user_list(request):
    users = Bot_user.objects.all()
    context = {'users': users}
    return render(request, 'user/list_users.html', context)

@login_required
def user_history(request, user_pk):
    requests = Request.objects.filter(Q(status = 'conf') | Q(status = 'cancel'), user__pk = user_pk).order_by('-pk')
    user = Bot_user.objects.get(pk=user_pk)
    context = {'list': requests, 'bot_user': user}
    return render(request, 'user/user_history.html', context)

@login_required
def user_get_excel(request):
    def overall_points(user):
        points = 0
        for r in Request.objects.filter(user=user, status = 'conf'):
            points += r.point * r.amount

        return points
    
    df = {'№': [], 'ID': [], 'Имя': [], 'Номер телефона': [], 'Username': [], 'Город': [], 'Баллы': [], 'Снял': [], 'Общий': []}
    
    df['№'] = list(range(1, len(Bot_user.objects.all())+1))
    df['ID'] = list(Bot_user.objects.all().values_list('user_id', flat=True))
    df['Имя'] = list(Bot_user.objects.all().values_list('name', flat=True))
    df['Номер телефона'] = list(Bot_user.objects.all().values_list('phone', flat=True))
    df['Username'] = list(Bot_user.objects.all().values_list('username', flat=True))
    df['Город'] = list(Bot_user.objects.all().values_list('city', flat=True))
    df['Баллы'] = list(Bot_user.objects.all().values_list('point', flat=True))
    for user in Bot_user.objects.all():
        df['Снял'].append(user.spent_for_prizes)
        df['Общий'].append(user.spent_for_prizes + user.point)

    # df['Баллы'] = [overall_points(user) for user in Bot_user.objects.all()]


    df = pd.DataFrame(df).set_index('№')
    df.to_excel('files/excel/user_list.xlsx')
    file = open('files/excel/user_list.xlsx', 'rb')
    return FileResponse(file)
    # return HttpResponse('')


def points_statistic(request):
    # users = Bot_user.objects.all()
    # list = Request.objects.filter(status='conf').values('user__name').annotate(
    #     total=F('user__point')).order_by('-total').values('user__pk', 'user__name', 'user__firstname', 'user__city', 'total', 'user__point')
    # n = 0
    # for l in list:
    #     user = Bot_user.objects.get(pk=l['user__pk'])
    #     list[n]['total'] = user.spent_for_prizes + user.point
    #     n += 1

    list = Bot_user.objects.filter().exclude(phone=None).order_by('-total')

    about = About.objects.get(pk=1)
    context = {'list': list, 'about': about}
    return render(request, 'user/statistic.html', context)


def user_change_point(request, pk):
    user = Bot_user.objects.get(pk=pk)
    form = UserChangePointForm()
    if request.method == 'POST':
        form = UserChangePointForm(request.POST)
        if form.is_valid():
            point = form.cleaned_data['point']
            user.point += int(point)
            if user.point < 0:
                messages.warning(request, 'Баллов не может быть меньше 0')
                user.point -= int(point)
                
            else:
                user.save()
                return redirect(user_list)
    
    context = {'form': form, 'bot_user': user}
    return render(request, 'user/user_change_point.html', context)