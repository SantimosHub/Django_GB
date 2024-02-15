from django.urls import path
from .views import fetch_customer_orders, fetch_ordered_products_by_period
from store_app.views import index


urlpatterns = [
    path('', index, name='index'),
    path('customer-orders/<int:customer_id>', fetch_customer_orders, name='customer_orders'),
    path('ordered-products-by-period/<int:customer_id>', fetch_ordered_products_by_period,
         name='ordered_products_by_period'),
]
