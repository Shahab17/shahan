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

from .models import Apartment
from .forms import ApartmentModelForm
#################################### ListView ############################  

##################### Rent ###################
class ApartmentForRentListView(ListView):
    template_name = 'apartment/apartment_rent.html'
    model = Apartment

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
class ApartmentForSaleListView(ListView):
    template_name = 'apartment/apartment_sale.html'
    model = Apartment

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
class ApartmentForExchangeListView(ListView):
    template_name = 'apartment/apartment_exchange.html'
    model = Apartment

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
class ApartmentDetailView(DetailView):  
    model = Apartment
    template_name = 'apartment/apartment_detail.html' 


#################################### Create ############################ 
class ApartmentCreateView(CreateView):
    template_name = 'apartment/apartment_create.html'
    form_class = ApartmentModelForm

    def form_valid(self, form):
        return super().form_valid(form)
#################################### Update ############################
class ApartmentUpdateView(UpdateView):
    model = Apartment
    template_name = 'apartment/apartment_create.html'
    form_class = ApartmentModelForm

    def form_valid(self, form):
        return super().form_valid(form)
#################################### Delete ############################

##################### Rent ###################
class ApartmentForRentDeleteView(DeleteView):  
    model = Apartment
    template_name = 'apartment/apartment_delete.html'
    
    def get_success_url(self):
        return reverse('apartment_rent')


##################### Sale ###################
class ApartmentForSaleDeleteView(DeleteView):  
    model = Apartment
    template_name = 'apartment/apartment_delete.html'
    
    def get_success_url(self):
        return reverse('apartment_sale')

##################### Exchange ###################
class ApartmentForExchangeDeleteView(DeleteView):  
    model = Apartment
    template_name = 'apartment/apartment_delete.html'
    
    def get_success_url(self):
        return reverse('apartment_exchange')


