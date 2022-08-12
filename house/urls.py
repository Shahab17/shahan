from django.urls import path

from house.views import (
    HouseForRentListView, 
    HouseForSaleListView,
    HouseForExchangeListView,
    HouseDetailView,
    HouseCreateView,
    HouseUpdateView,
    HouseForRentDeleteView,
    HouseForSaleDeleteView,
    HouseForExchangeDeleteView
)
urlpatterns = [
    ######################### List-View ############################
    path('rent/', HouseForRentListView.as_view(), name='house_rent'),
    path('sale/', HouseForSaleListView.as_view(), name='house_sale'),
    path('exchange/', HouseForExchangeListView.as_view(), name='house_exchange'),
    
    ######################### Detail, Create and Update -View ############################
    path('detail/<int:pk>/', HouseDetailView.as_view(), name='house_detail'),
    path('create/', HouseCreateView.as_view(), name='house_create'),
    path('update/<int:pk>/', HouseUpdateView.as_view(), name='house_update'),
    
    ######################### Delete-View ############################
    path('delete-rent/<int:pk>/', HouseForRentDeleteView.as_view(), name='house_delete_rent'),
    
    path('delete-sale/<int:pk>/', HouseForSaleDeleteView.as_view(), name='house_delete_sale'),
    
    path('delete-exchange/<int:pk>/', HouseForExchangeDeleteView.as_view(), name='house_delete_exchange'),

]