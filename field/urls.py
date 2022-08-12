from django.urls import path

from field.views import (
    FieldForRentListView, 
    FieldForSaleListView,
    FieldForExchangeListView,
    FieldDetailView,
    FieldCreateView,
    FieldUpdateView,
    FieldForRentDeleteView,
    FieldForSaleDeleteView,
    FieldForExchangeDeleteView
)
urlpatterns = [
    ######################### List-View ############################
    path('rent/', FieldForRentListView.as_view(), name='field_rent'),
    path('sale/', FieldForSaleListView.as_view(), name='field_sale'),
    path('exchange/', FieldForExchangeListView.as_view(), name='field_exchange'),
    
    ######################### Detail, Create and Update -View ############################
    path('detail/<int:pk>/', FieldDetailView.as_view(), name='field_detail'),
    path('create/', FieldCreateView.as_view(), name='field_create'),
    path('update/<int:pk>/', FieldUpdateView.as_view(), name='field_update'),
    
    ######################### Delete-View ############################
    path('delete-rent/<int:pk>/', FieldForRentDeleteView.as_view(), name='field_delete_rent'),
    
    path('delete-sale/<int:pk>/', FieldForSaleDeleteView.as_view(), name='field_delete_sale'),
    
    path('delete-exchange/<int:pk>/', FieldForExchangeDeleteView.as_view(), name='field_delete_exchange'),

]