from django.http import HttpResponse, FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required

from django.db.models.functions import TruncDay
from django.db.models import Count

from datetime import datetime, timedelta
from app.models import *
from app.forms import *
from django.db.models import Count, Sum, F


@login_required
def user_list(request):
    users = Bot_user.objects.all()
    context = {'users': users}
    return render(request, 'user/list_users.html', context)

@login_required
def user_history(request, user_pk):
    requests = Request.objects.filter(status = 'conf', user__pk = user_pk)
    user = Bot_user.objects.get(pk=user_pk).name
    context = {'list': requests, 'user': user}
    return render(request, 'user/user_history.html', context)


def points_statistic(request):
    # users = Bot_user.objects.all()
    list = Request.objects.filter(status='conf').values('user__name').annotate(
        total=Sum(F('point') * F('amount'))).order_by('-total').values('user__name', 'user__firstname', 'total')

    context = {'list': list}
    return render(request, 'user/statistic.html', context)