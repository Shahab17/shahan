from django.urls import path

from store.views import (
    StoreForRentListView, 
    StoreForSaleListView,
    StoreForExchangeListView,
    StoreDetailView,
    StoreCreateView,
    StoreUpdateView,
    StoreForRentDeleteView,
    StoreForSaleDeleteView,
    StoreForExchangeDeleteView
)
urlpatterns = [
    ######################### List-View ############################
    path('rent/', StoreForRentListView.as_view(), name='store_rent'),
    path('sale/', StoreForSaleListView.as_view(), name='store_sale'),
    path('exchange/', StoreForExchangeListView.as_view(), name='store_exchange'),
    
    ######################### Detail, Create and Update -View ############################
    path('detail/<int:pk>/', StoreDetailView.as_view(), name='store_detail'),
    path('create/', StoreCreateView.as_view(), name='store_create'),
    path('update/<int:pk>/', StoreUpdateView.as_view(), name='store_update'),
    
    ######################### Delete-View ############################
    path('delete-rent/<int:pk>/', StoreForRentDeleteView.as_view(), name='store_delete_rent'),
    
    path('delete-sale/<int:pk>/', StoreForSaleDeleteView.as_view(), name='store_delete_sale'),
    
    path('delete-exchange/<int:pk>/', StoreForExchangeDeleteView.as_view(), name='store_delete_exchange'),

]