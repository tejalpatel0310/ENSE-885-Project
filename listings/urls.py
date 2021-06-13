from django.urls import path
from . import views
from . views import AddListingview


urlpatterns = [
    path('', views.index, name='listings'),
    path('addlisting', AddListingview.as_view(), name='addlisting'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]

