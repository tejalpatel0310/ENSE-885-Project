from django.contrib import admin
<<<<<<< HEAD
from .models import Listing, LandownerListingsModel
=======
from .models import Listing
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('list_date',)
    list_editable = ('is_published',)


<<<<<<< HEAD
class LandownersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('list_date',)
    list_editable = ('is_published',)


admin.site.register(Listing, ListingAdmin)
admin.site.register(LandownerListingsModel, LandownersAdmin)

=======
admin.site.register(Listing, ListingAdmin)
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b


