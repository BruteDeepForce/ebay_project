# ebay_integration/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('add-product/', views.add_ebay_product, name='add-product'),
]
