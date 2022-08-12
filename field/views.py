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

from .models import Field
from .forms import FieldModelForm
#################################### ListView ############################  

##################### Rent ###################
class FieldForRentListView(ListView):
    template_name = 'field/field_rent.html'
    model = Field

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
class FieldForSaleListView(ListView):
    template_name = 'field/field_sale.html'
    model = Field

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
class FieldForExchangeListView(ListView):
    template_name = 'field/field_exchange.html'
    model = Field

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
class FieldDetailView(DetailView):  
    model = Field
    template_name = 'field/field_detail.html' 


#################################### Create ############################ 
class FieldCreateView(CreateView):
    template_name = 'field/field_create.html'
    form_class = FieldModelForm

    def form_valid(self, form):
        return super().form_valid(form)
#################################### Update ############################
class FieldUpdateView(UpdateView):
    model = Field
    template_name = 'field/field_create.html'
    form_class = FieldModelForm

    def form_valid(self, form):
        return super().form_valid(form)
#################################### Delete ############################

##################### Rent ###################
class FieldForRentDeleteView(DeleteView):  
    model = Field
    template_name = 'field/field_delete.html'
    
    def get_success_url(self):
        return reverse('field_rent')


##################### Sale ###################
class FieldForSaleDeleteView(DeleteView):  
    model = Field
    template_name = 'field/field_delete.html'
    
    def get_success_url(self):
        return reverse('field_sale')

##################### Exchange ###################
class FieldForExchangeDeleteView(DeleteView):  
    model = Field
    template_name = 'field/field_delete.html'
    
    def get_success_url(self):
        return reverse('field_exchange')


