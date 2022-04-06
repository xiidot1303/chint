from django.contrib import admin
from app.models import *

class Bot_userAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'phone', 'lang')
    search_fields = ('user_id', 'name', 'phone')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'point')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'amount', 'photo', 'point', 'status')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('action', 'contact')

admin.site.register(Bot_user, Bot_userAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(About, AboutAdmin)