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

from .models import House
from .forms import HouseModelForm
#################################### ListView ############################  

##################### Rent ###################
class HouseForRentListView(ListView):
    template_name = 'house/house_rent.html'
    model = House

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
class HouseForSaleListView(ListView):
    template_name = 'house/house_sale.html'
    model = House

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
class HouseForExchangeListView(ListView):
    template_name = 'house/house_exchange.html'
    model = House

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
class HouseDetailView(DetailView):  
    model = House
    template_name = 'house/house_detail.html' 


#################################### Create ############################ 
class HouseCreateView(CreateView):
    template_name = 'house/house_create.html'
    form_class = HouseModelForm

    def form_valid(self, form):
        return super().form_valid(form)
#################################### Update ############################
class HouseUpdateView(UpdateView):
    model = House
    template_name = 'house/house_create.html'
    form_class = HouseModelForm

    def form_valid(self, form):
        return super().form_valid(form)
#################################### Delete ############################

##################### Rent ###################
class HouseForRentDeleteView(DeleteView):  
    model = House
    template_name = 'house/house_delete.html'
    
    def get_success_url(self):
        return reverse('house_rent')


##################### Sale ###################
class HouseForSaleDeleteView(DeleteView):  
    model = House
    template_name = 'house/house_delete.html'
    
    def get_success_url(self):
        return reverse('house_sale')

##################### Exchange ###################
class HouseForExchangeDeleteView(DeleteView):  
    model = House
    template_name = 'house/house_delete.html'
    
    def get_success_url(self):
        return reverse('house_exchange')


