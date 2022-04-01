from django.contrib import admin
from app.models import *

class Bot_userAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'phone', 'lang')
    search_fields = ('user_id', 'name', 'phone')



admin.site.register(Bot_user, Bot_userAdmin)