from django.http import HttpResponse, FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.db.models.functions import TruncDay
from django.db.models import Count, Sum

from datetime import datetime, timedelta
from app.models import *


@login_required
def main_menu(request):
    return render(request, 'main/main_menu.html')


@login_required
def get_photos(request, folder, subfolder, file):
    f = open('files/{}/{}/{}'.format(folder, subfolder, file), 'rb')
    return FileResponse(f)

