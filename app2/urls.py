from django.urls import path, include
from app2.views import main, product, request, user, administration, prize, laureate


urlpatterns = [
    # main
    path('', request.request_list, name='main_menu'),

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


]
