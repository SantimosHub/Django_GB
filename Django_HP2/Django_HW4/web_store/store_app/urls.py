from django.urls import path
from .views import fetch_customer_orders, fetch_ordered_products_by_period, add_product, edit_product
from store_app.views import index


urlpatterns = [
    path('', index, name='index'),
    path('customer-orders/<int:customer_id>', fetch_customer_orders, name='customer_orders'),
    path('ordered-products-by-period/<int:customer_id>', fetch_ordered_products_by_period,
         name='ordered_products_by_period'),
    path('add/', add_product, name='add_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
]
