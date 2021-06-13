from django.contrib import admin
from .models import Listing, LandownerListingsModel
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('list_date',)
    list_editable = ('is_published',)


class LandownersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('list_date',)
    list_editable = ('is_published',)


admin.site.register(Listing, ListingAdmin)
admin.site.register(LandownerListingsModel, LandownersAdmin)



