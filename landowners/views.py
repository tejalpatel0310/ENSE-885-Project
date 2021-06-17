from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from landowners.models import LandownerListingsModel,RegisterLandownerModel
from . forms import *
# Create your views here.

class Indexview(LoginRequiredMixin, ListView):
    model = LandownerListingsModel
    context_object_name = 'listings'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        listingid = self.request.user.listing_id
        context['listings'] = context['listings'].filter(listing_id=listingid)
        return context


class AddListingview(CreateView):
    model = LandownerListingsModel
    form_class = LandownerListingForm
    template_name = 'addlisting.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.ngo = self.request.user
        return super(AddListingview, self).form_valid(form)

class EditListingview(LoginRequiredMixin, UpdateView):
    model = LandownerListingsModel
    form_class = LandownerListingForm
    template_name = 'addlisting.html'
    success_url = reverse_lazy('index')


class DeleteListingview(LoginRequiredMixin, DeleteView):
    model = LandownerListingsModel
    context_object_name = 'listings'
    template_name = 'deletelisting.html'
    success_url = reverse_lazy('index')



##def addlisting(request):
  ##  return render(request, 'addlisting.html')

