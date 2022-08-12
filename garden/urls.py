from django.urls import path

from garden.views import (
    GardenForRentListView, 
    GardenForSaleListView,
    GardenForExchangeListView,
    GardenDetailView,
    GardenCreateView,
    GardenUpdateView,
    GardenForRentDeleteView,
    GardenForSaleDeleteView,
    GardenForExchangeDeleteView
)
urlpatterns = [
    ######################### List-View ############################
    path('rent/', GardenForRentListView.as_view(), name='garden_rent'),
    path('sale/', GardenForSaleListView.as_view(), name='garden_sale'),
    path('exchange/', GardenForExchangeListView.as_view(), name='garden_exchange'),
    
    ######################### Detail, Create and Update -View ############################
    path('detail/<int:pk>/', GardenDetailView.as_view(), name='garden_detail'),
    path('create/', GardenCreateView.as_view(), name='garden_create'),
    path('update/<int:pk>/', GardenUpdateView.as_view(), name='garden_update'),
    
    ######################### Delete-View ############################
    path('delete-rent/<int:pk>/', GardenForRentDeleteView.as_view(), name='garden_delete_rent'),
    
    path('delete-sale/<int:pk>/', GardenForSaleDeleteView.as_view(), name='garden_delete_sale'),
    
    path('delete-exchange/<int:pk>/', GardenForExchangeDeleteView.as_view(), name='garden_delete_exchange'),

]