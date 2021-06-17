from django.urls import path
from . views import AddListingview, EditListingview, DeleteListingview

urlpatterns = [
    path('', AddListingview.as_view(), name='addlisting'),
    path('editlisting/', EditListingview.as_view(), name='editlisting'),
    path('deletelisting', DeleteListingview.as_view(), name='deletelisting'),
]