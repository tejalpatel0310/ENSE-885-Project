from django.shortcuts import render
<<<<<<< HEAD
from listings.models import Listing, LandownerListingsModel
=======
from listings.models import Listing
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
from listings.choices import price_choices,state_choices,lot_size_choices
from listings.views import listing


def index(request):

<<<<<<< HEAD
     listings =LandownerListingsModel .objects.order_by('-list_date').filter(is_published=True)[:3]
=======
     listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b

     context = {
          'listings' : listings,
          'state_choices': state_choices,
          'lot_size_choices': lot_size_choices,
          'price_choices': price_choices,
     }

     return render(request, 'pages/index.html', context)


def about(request):
     return render(request, 'pages/about.html')




