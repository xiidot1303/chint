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
def product_list(request):
    products = Product.objects.all().order_by('-pk')
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

@login_required
def product_upload_by_excel(request):
    if request.method == 'POST':
        bbf = UploadFileFrom(request.POST, request.FILES)
        if bbf.is_valid():
            Excel.objects.get_or_create(pk=1)
            excel = Excel.objects.get(pk=1)
            excel.file = bbf.cleaned_data['file']
            excel.save()
            try:
                book = xlrd.open_workbook('files/{}'.format(str(excel.file)))
                sh = book.sheet_by_index(0)

                nrows = sh.nrows
                for row in range(1, nrows):
                    values = sh.row_values(row)
                    title = values[0]
                    description = values[1]
                    point = values[2]
                    Product.objects.create(title=title, description=description, point=point)
                messages.success(request, 'Успешно добавлено')
            except:
                messages.warning(request, 'Ошибка')

    else:
        bbf = UploadFileFrom()
    if Excel.objects.all():
        file_path = Excel.objects.all()[0].file
    else:
        file_path = ''
    return render(request, 'product/product_upload.html', {'form': bbf, 'file_path': file_path})
