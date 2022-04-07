from django.db import models

class Bot_user(models.Model):
    user_id = models.IntegerField(null=True)
    name = models.CharField(null=True, blank=True, max_length=200)
    username = models.CharField(null=True, blank=True, max_length=200)
    firstname = models.CharField(null=True, blank=True, max_length=500)
    phone = models.CharField(null=True, blank=True, max_length=40)
    lang = models.CharField(null=True, blank=True, max_length=5)
    date = models.DateTimeField(db_index = True, null=True, auto_now_add=True, blank=True)
    point = models.FloatField(null=True, blank=True)
    def __str__(self) -> str:
        try:
            return self.name + ' ' + str(self.phone)
        except:
            return super().__str__()

class Product(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True, max_length=1000)
    photo = models.FileField(upload_to='photos/products', null=True, blank=True)
    point = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Request(models.Model): # to get points
    user = models.ForeignKey('Bot_user', null=True, blank=False, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.PROTECT)
    amount = models.FloatField(null=True, blank=True)
    photo = models.FileField(upload_to='photos/requests', null=True, blank=True)
    point = models.FloatField(null=True, blank=True) # after calculate point by [amount] * [product.point], save it, because product will may be changed
    status = models.CharField(null=True, blank=True, max_length=20, choices=(('wait', 'waiting'), ('cancel', 'cancelled'), ('conf', 'confirmed')))
    

class About(models.Model):
    action = models.TextField(null=True, blank=True, max_length=500)
    file = models.FileField(upload_to='about', null=True, blank=True)
    contact = models.TextField(null=True, blank=True, max_length=500)