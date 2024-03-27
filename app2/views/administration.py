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


class AboutEditView(LoginRequiredMixin, UpdateView):
    model = About
    form_class = AboutForm
    template_name = 'administration/about_update.html'
    success_url = '/app2/about/update/1/'
    
class RuleEditView(LoginRequiredMixin, UpdateView):
    model = Rule
    form_class = RuleForm
    template_name = 'administration/rule_update.html'
    success_url = '/rule/update/1/'
