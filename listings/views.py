from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from .models import Listing, LandownerListingsModel
from django.urls import reverse_lazy
from . forms import *
from django.views.generic import CreateView
=======
from .models import Listing
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, state_choices, lot_size_choices

# Create your views here.
<<<<<<< HEAD
class AddListingview(CreateView):
    model = LandownerListingsModel
    form_class = LandownerListingForm
    template_name = 'listings/addlisting.html'
    success_url = reverse_lazy('listings')

def index(request):
    listings = LandownerListingsModel.objects.order_by('-list_date').filter(is_published=True)
=======

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b

    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


<<<<<<< HEAD
def listing(request, listing_id):
    listing = get_object_or_404(LandownerListingsModel, pk=listing_id)
=======
def listing(request, listing_id ):
    listing = get_object_or_404(Listing, pk=listing_id)
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b

    # getting internal photos
    internal_photos = []
    for i in range(1, 4):
        if getattr(listing, 'photo_%d' % i):
            photo = getattr(listing, 'photo_%d' % i)
            internal_photos.append(photo)

    context = {
<<<<<<< HEAD
        'listing': listing,
=======
        'listing' : listing,
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
        'internal_photos': internal_photos
    }
    return render(request, 'listings/listing.html', context)


def search(request):
<<<<<<< HEAD
    queryset_list = LandownerListingsModel.objects.order_by('-list_date')
=======
    queryset_list = Listing.objects.order_by('-list_date')
>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b

    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #state
    if 'state' in request.GET:
       state = request.GET['state']
       if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    #acres
    if 'lot_size' in request.GET:
        lot_size = request.GET['lot_size']
        if lot_size:
            queryset_list = queryset_list.filter(lot_size__lte = lot_size)

<<<<<<< HEAD
=======

>>>>>>> 59884a17a2d04919bfa7298b25771eddb0b3788b
    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte= price)

    context = {
        'state_choices': state_choices,
        'lot_size_choices': lot_size_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)

