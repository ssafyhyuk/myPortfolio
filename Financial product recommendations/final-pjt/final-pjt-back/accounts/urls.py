from django.urls import path
from . import views

urlpatterns = [
    path('deposit-products-list/', views.deposit_products_list),
    path('saving-products-list/', views.saving_products_list),
    path('update-user/', views.update_user),
]
