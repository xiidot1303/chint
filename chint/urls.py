"""chint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView

from app.views.botwebhook import bot_webhook
from app.views import main, product, request, user, administration, prize, laureate

from config import TELEGRAM_BOT_API_TOKEN, ENVIRONMENT


urlpatterns = [
    #admin
    path('xiidot1303/', admin.site.urls),
    path(TELEGRAM_BOT_API_TOKEN, bot_webhook),

    # auth
    path('accounts/login/', LoginView.as_view()),
    path('changepassword/', PasswordChangeView.as_view(template_name = 'registration/change_password.html'), name='editpassword'),
    path('changepassword/done/', PasswordChangeDoneView.as_view(template_name = 'registration/afterchanging.html'), name='password_change_done'),
    # path('profile', change_profile, name = "change_profile"),
    path('logout/', LogoutView.as_view(), name='logout'),

    # main
    path('', request.request_list, name='main_menu'),

    # get file
    path('files/<str:folder>/<str:subfolder>/<str:file>/', main.get_photos, name='get_photo'),
    

    # product
    path('product/list', product.product_list, name='product_list'),
    path('product/create', product.ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', product.ProductEditView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', product.product_delete, name='product_delete'),
    path('product/upload', product.product_upload_by_excel, name='product_upload'),

    # request
    path('request/list', request.request_list, name='request_list'),
    path('request/change_status/<int:pk>/<str:status>/', request.request_change_status, name='request_change_status'),

    # user
    path('user/list', user.user_list, name='user_list'),
    path('user/history/<int:user_pk>/', user.user_history, name='user_history'),
    path('user/change/point/<int:pk>/', user.user_change_point, name='user_change_point'),
    path('statistic', user.points_statistic, name='statistic'),
        # get excel
    path('user/get/excel', user.user_get_excel, name='user_get_excel'),

    # administration
    path('about/update/<int:pk>/', administration.AboutEditView.as_view(), name='about_update'),
    path('rule/update/<int:pk>/', administration.RuleEditView.as_view(), name='rule_update'),

    # prize
    path('prize/list', prize.prize_list, name='prize_list'),
    path('prize/create', prize.PrizeCreateView.as_view(), name='prize_create'),
    path('prize/update/<int:pk>/', prize.PrizeEditView.as_view(), name='prize_update'),
    path('prize/delete/<int:pk>/', prize.prize_delete, name='prize_delete'),

    # laureate
    path('laureate/list', laureate.laureate_list, name='laureate_list'),
    path('laureate/change_status/<int:pk>/<str:status>/', laureate.laureate_change_status, name='laureate_change_status'),
    path('laureate/delete/<str:pk>/', laureate.laureate_delete, name='laureate_delete'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static('/files/', document_root = 'files/')
