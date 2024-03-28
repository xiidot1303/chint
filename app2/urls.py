from django.urls import path, include
from app2.views import main, request, user, administration, prize, laureate


urlpatterns = [
    # main
    path('', request.request_list, name='main_menu2'),

    # request
    path('request/list', request.request_list, name='request_list2'),
    path('request/change_status/<int:pk>/<str:status>/', request.request_change_status, name='request_change_status2'),

    # user
    path('user/list', user.user_list, name='user_list2'),
    path('user/history/<int:user_pk>/', user.user_history, name='user_history2'),
    path('user/change/point/<int:pk>/', user.user_change_point, name='user_change_point2'),
    path('statistic', user.points_statistic, name='statistic2'),
        # get excel
    path('user/get/excel', user.user_get_excel, name='user_get_excel2'),

    # administration
    path('about/update/<int:pk>/', administration.AboutEditView.as_view(), name='about_update2'),
    path('rule/update/<int:pk>/', administration.RuleEditView.as_view(), name='rule_update2'),

    # prize
    path('prize/list', prize.prize_list, name='prize_list2'),
    path('prize/create', prize.PrizeCreateView.as_view(), name='prize_create2'),
    path('prize/update/<int:pk>/', prize.PrizeEditView.as_view(), name='prize_update2'),
    path('prize/delete/<int:pk>/', prize.prize_delete, name='prize_delete2'),

    # laureate
    path('laureate/list', laureate.laureate_list, name='laureate_list2'),
    path('laureate/change_status/<int:pk>/<str:status>/', laureate.laureate_change_status, name='laureate_change_status2'),
    path('laureate/delete/<str:pk>/', laureate.laureate_delete, name='laureate_delete2'),


]
