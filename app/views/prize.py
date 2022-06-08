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
import xlrd

@login_required
def prize_list(request):
    prizes = Prize.objects.all().order_by('-pk')
    context = {'prizes': prizes}
    return render(request, 'prize/list_prize.html', context)

class PrizeCreateView(CreateView, LoginRequiredMixin):
    template_name = 'prize/create_prize.html'
    form_class = PrizeForm
    success_url = '/prize/list'

class PrizeEditView(UpdateView, LoginRequiredMixin):
    model = Prize
    form_class = PrizeForm
    template_name = 'prize/update_prize.html'
    success_url = '/prize/list'

@login_required
def prize_delete(request, pk):
    obj = Prize.objects.get(pk=pk)
    obj.delete()
    return redirect(prize_list)
