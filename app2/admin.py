from django.contrib import admin
from app2.models import *

class PrizeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo', 'point')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'photo', 'point', 'status')

class PrizewinnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'prize', 'amount', 'point', 'status')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('action', 'contact_ru', 'company_name', 'site')

class RuleAdmin(admin.ModelAdmin):
    list_display = ('text_ru', 'file_ru')



admin.site.register(Prize, PrizeAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(Prizewinner, PrizewinnerAdmin)