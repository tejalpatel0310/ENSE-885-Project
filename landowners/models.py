from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#for register landowners
class RegisterLandownerModel(User):

    Landowner_id = models.BigAutoField(primary_key=True)
    contact_number = models.CharField(max_length=15, default="")
    description = models.TextField(blank=True)

    def __str__(self):
     return self.username


#add landowner activity
class LandownerListingsModel(models.Model):

    class SaleType(models.TextChoices):
        FOR_RENT = 'for Rent'
        FOR_LEASE = 'for Lease'

    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    price = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    sale_type = models.CharField(max_length=50, choices = SaleType.choices, default = SaleType.FOR_RENT)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    #date = models.DateField()
    #time = models.TimeField()
    complete = models.BooleanField(default=False)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ['complete']






