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

from .models import Store
from .forms import StoreModelForm
#################################### ListView ############################  

##################### Rent ###################
class StoreForRentListView(ListView):
    template_name = 'store/store_rent.html'
    model = Store

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
class StoreForSaleListView(ListView):
    template_name = 'store/store_sale.html'
    model = Store

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
class StoreForExchangeListView(ListView):
    template_name = 'store/store_exchange.html'
    model = Store

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
class StoreDetailView(DetailView):  
    model = Store
    template_name = 'store/store_detail.html' 


#################################### Create ############################ 
class StoreCreateView(CreateView):
    template_name = 'store/store_create.html'
    form_class = StoreModelForm

    def form_valid(self, form):
        return super().form_valid(form)
#################################### Update ############################
class StoreUpdateView(UpdateView):
    model = Store
    template_name = 'store/store_create.html'
    form_class = StoreModelForm

    def form_valid(self, form):
        return super().form_valid(form)
#################################### Delete ############################

##################### Rent ###################
class StoreForRentDeleteView(DeleteView):  
    model = Store
    template_name = 'store/store_delete.html'
    
    def get_success_url(self):
        return reverse('store_rent')


##################### Sale ###################
class StoreForSaleDeleteView(DeleteView):  
    model = Store
    template_name = 'store/store_delete.html'
    
    def get_success_url(self):
        return reverse('store_sale')

##################### Exchange ###################
class StoreForExchangeDeleteView(DeleteView):  
    model = Store
    template_name = 'store/store_delete.html'
    
    def get_success_url(self):
        return reverse('store_exchange')


