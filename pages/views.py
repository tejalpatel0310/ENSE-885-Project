from django.shortcuts import render
from listings.models import Listing, LandownerListingsModel
from listings.choices import price_choices,state_choices,lot_size_choices
from listings.views import listing


def index(request):

     listings =LandownerListingsModel .objects.order_by('-list_date').filter(is_published=True)[:3]

     context = {
          'listings' : listings,
          'state_choices': state_choices,
          'lot_size_choices': lot_size_choices,
          'price_choices': price_choices,
     }

     return render(request, 'pages/index.html', context)


def about(request):
     return render(request, 'pages/about.html')




