from django.shortcuts import render
from django.urls import reverse

from django.db.models import Q

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView

)

from .models import Garden
from .forms import GardenModelForm
#################################### ListView ############################  

##################### Rent ###################
class GardenForRentListView(ListView):
    template_name = 'garden/garden_rent.html'
    model = Garden

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(kind = 1).filter(
                Q(address__icontains = query) |
                Q(area__icontains = query) |
                Q(year__icontains = query) |
                Q(rent_price1__icontains = query) |
                Q(rent_price2__icontains = query)
                ).distinct
        else:
            object_list = self.model.objects.filter(kind = 1)
        return object_list
##################### Sale ###################
class GardenForSaleListView(ListView):
    template_name = 'garden/garden_sale.html'
    model = Garden

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(kind = 2).filter(
                Q(address__icontains = query) |
                Q(area__icontains = query) |
                Q(year__icontains = query) |
                Q(rent_price1__icontains = query) |
                Q(rent_price2__icontains = query)
                ).distinct
        else:
            object_list = self.model.objects.filter(kind = 2)
        return object_list
    
##################### Exchange ###################
class GardenForExchangeListView(ListView):
    template_name = 'garden/garden_exchange.html'
    model = Garden

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(kind = 3).filter(
                Q(address__icontains = query) |
                Q(area__icontains = query) |
                Q(year__icontains = query) |
                Q(rent_price1__icontains = query) |
                Q(rent_price2__icontains = query)
                ).distinct
        else:
            object_list = self.model.objects.filter(kind = 3)
        return object_list

#################################### Detail ############################ 
class GardenDetailView(DetailView):  
    model = Garden
    template_name = 'garden/garden_detail.html' 


#################################### Create ############################ 
class GardenCreateView(CreateView):
    template_name = 'garden/garden_create.html'
    form_class = GardenModelForm

    def form_valid(self, form):
        return super().form_valid(form)
#################################### Update ############################
class GardenUpdateView(UpdateView):
    model = Garden
    template_name = 'garden/garden_create.html'
    form_class = GardenModelForm

    def form_valid(self, form):
        return super().form_valid(form)
#################################### Delete ############################

##################### Rent ###################
class GardenForRentDeleteView(DeleteView):  
    model = Garden
    template_name = 'garden/garden_delete.html'
    
    def get_success_url(self):
        return reverse('garden_rent')


##################### Sale ###################
class GardenForSaleDeleteView(DeleteView):  
    model = Garden
    template_name = 'garden/garden_delete.html'
    
    def get_success_url(self):
        return reverse('garden_sale')

##################### Exchange ###################
class GardenForExchangeDeleteView(DeleteView):  
    model = Garden
    template_name = 'garden/garden_delete.html'
    
    def get_success_url(self):
        return reverse('garden_exchange')


