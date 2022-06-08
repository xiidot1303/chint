from django.contrib import admin
from app.models import *

class Bot_userAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'phone', 'lang', 'point')
    search_fields = ('user_id', 'name', 'phone')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'point')

class PrizeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'point')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'amount', 'photo', 'point', 'status')

class PrizewinnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'prize', 'amount', 'point', 'status')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('action', 'contact_ru', 'company_name', 'site')

class RuleAdmin(admin.ModelAdmin):
    list_display = ('text_ru', 'file_ru')



admin.site.register(Bot_user, Bot_userAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(Prizewinner, PrizewinnerAdmin)