from django.db import models
from datetime import datetime
<<<<<<< HEAD
# Create your models here.

#showing listing on pages
=======
from landowners.models import LandownerListingsModel
# Create your models here.

#showing listing on pages


>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_RENT = 'for Rent'
        FOR_LEASE = 'for Lease'

    #landowner_id = models.ForeignKey(LandownerListingsModel, on_delete=models.DO_NOTHING, default="")
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    sale_type = models.CharField(max_length=50, choices = SaleType.choices, default = SaleType.FOR_RENT)
    contact_number = models.CharField(max_length=15, blank=False, default="")
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
<<<<<<< HEAD



#add landowner listing
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
    contact_number = models.CharField(max_length=15, blank=False, default="")
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
         return self.title

    class Meta:
        ordering = ['complete']

=======
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
