from django.db import models
from django.db.models import Q



class Request(models.Model): # to get points
    user = models.ForeignKey('app.Bot_user', null=True, blank=False, on_delete=models.PROTECT, related_name='app2_bot_user')
    amount = models.FloatField(null=True, blank=True)
    store = models.CharField(null=True, blank=True, max_length=255)
    photo = models.FileField(upload_to='photos/requests', null=True, blank=True)
    photo2 = models.FileField(upload_to='photos/requests', null=True, blank=True)
    point = models.FloatField(null=True, blank=True)
    status = models.CharField(null=True, blank=True, max_length=20, choices=(('wait', 'waiting'), ('cancel', 'cancelled'), ('conf', 'confirmed')))
    date = models.DateTimeField(null=True, blank=True)

class About(models.Model):
    action = models.TextField(null=True, blank=True, max_length=500)
    file_ru = models.FileField(upload_to='about', null=True, blank=True)
    file_uz = models.FileField(upload_to='about', null=True, blank=True)
    contact_ru = models.TextField(null=True, blank=True, max_length=500)
    contact_uz = models.TextField(null=True, blank=True, max_length=500)
    telegram_username = models.CharField(null=True, blank=True, max_length=200)

    # footer
    company_name = models.CharField(null=True, blank=True, max_length=200)
    company_about = models.CharField(null=True, blank=True, max_length=200)
    phone1 = models.CharField(null=True, blank=True, max_length=200)
    phone2 = models.CharField(null=True, blank=True, max_length=200)
    site = models.CharField(null=True, blank=True, max_length=200)
    email = models.CharField(null=True, blank=True, max_length=200)
    instagram = models.CharField(null=True, blank=True, max_length=200)
    facebook = models.CharField(null=True, blank=True, max_length=200)
    telegram = models.CharField(null=True, blank=True, max_length=200)
    youtube = models.CharField(null=True, blank=True, max_length=200)

class Rule(models.Model):
    file_uz = models.FileField(upload_to='rule', null=True, blank=True)
    file_ru = models.FileField(upload_to='rule', null=True, blank=True)
    text_uz = models.TextField(null=True, blank=True, max_length=1000)
    text_ru = models.TextField(null=True, blank=True, max_length=1000)

class Excel(models.Model):
    file = models.FileField(upload_to='excel/', null=True, blank=True)


class Prize(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    title_uz = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True, max_length=1000)
    description_uz = models.TextField(null=True, blank=True, max_length=1000)
    photo = models.FileField(upload_to='photos/prizes', null=True, blank=True)
    point = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
class Prizewinner(models.Model):
    user = models.ForeignKey('app.Bot_user', null=True, blank=False, on_delete=models.PROTECT, related_name='app2_prizewinner_bot_user')
    prize = models.ForeignKey('app2.Prize', null=True, blank=True, on_delete=models.PROTECT)
    amount = models.FloatField(null=True, blank=True)
    point = models.FloatField(null=True, blank=True) # after calculate point by [amount] * [prize.point], save it, because prize will may be changed
    status = models.CharField(null=True, blank=True, max_length=20, choices=(
        ('wait', 'waiting'), ('cancel', 'cancelled'), ('conf', 'confirmed'), ('end', 'end')
    ))
    
    def save(self, *args, **kwargs):
        super(Prizewinner, self).save(*args, **kwargs)
        user = self.user
        user.total = user.point + user.spent_for_prizes
        user.save()