from django.urls import path
from . import views
<<<<<<< HEAD
from . views import AddListingview
=======
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b


urlpatterns = [
    path('', views.index, name='listings'),
<<<<<<< HEAD
    path('addlisting', AddListingview.as_view(), name='addlisting'),
=======
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]

