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
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/list_product.html', context)


class ProductCreateView(CreateView, LoginRequiredMixin):
    template_name = 'product/create_product.html'
    form_class = ProductForm
    success_url = '/product/list'

class ProductEditView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'product/update_product.html'
    success_url = '/product/list'

@login_required
def product_delete(request, pk):
    obj = Product.objects.get(pk=pk)
    obj.delete()
    return redirect(product_list)