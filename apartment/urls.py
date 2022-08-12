from django.urls import path

from apartment.views import (
    ApartmentForRentListView, 
    ApartmentForSaleListView,
    ApartmentForExchangeListView,
    ApartmentDetailView,
    ApartmentCreateView,
    ApartmentUpdateView,
    ApartmentForRentDeleteView,
    ApartmentForSaleDeleteView,
    ApartmentForExchangeDeleteView
)
urlpatterns = [
    ######################### List-View ############################
    path('rent/', ApartmentForRentListView.as_view(), name='apartment_rent'),
    path('sale/', ApartmentForSaleListView.as_view(), name='apartment_sale'),
    path('exchange/', ApartmentForExchangeListView.as_view(), name='apartment_exchange'),
    
    ######################### Detail, Create and Update -View ############################
    path('detail/<int:pk>/', ApartmentDetailView.as_view(), name='apartment_detail'),
    path('create/', ApartmentCreateView.as_view(), name='apartment_create'),
    path('update/<int:pk>/', ApartmentUpdateView.as_view(), name='apartment_update'),
    
    ######################### Delete-View ############################
    path('delete-rent/<int:pk>/', ApartmentForRentDeleteView.as_view(), name='apartment_delete_rent'),
    
    path('delete-sale/<int:pk>/', ApartmentForSaleDeleteView.as_view(), name='apartment_delete_sale'),
    
    path('delete-exchange/<int:pk>/', ApartmentForExchangeDeleteView.as_view(), name='apartment_delete_exchange'),

]