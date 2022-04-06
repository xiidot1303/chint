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



@login_required
def request_list(request):
    requests = Request.objects.filter(status='wait')
    context = {'list': requests}
    return render(request, 'request/list_request.html', context)

@login_required
def request_change_status(request, pk, status):
    obj = Request.objects.get(pk=pk)
    obj.status = status
    obj.save()
    return redirect(request_list)
