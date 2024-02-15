from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Customer, Order


def index(request):
    context = {
        'title': 'Our store',
    }
    return render(request, 'store_app/index.html', context)


def fetch_customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    context = {
        'customer': customer,
        'orders': orders,
    }
    return render(request, 'store_app/orders.html', context)


def fetch_ordered_products_by_period(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)

    orders_week = Order.objects.filter(customer=customer, order_date__gte=week_ago)
    orders_month = Order.objects.filter(customer=customer, order_date__gte=month_ago)
    orders_year = Order.objects.filter(customer=customer, order_date__gte=year_ago)

    products_week = set()
    products_month = set()
    products_year = set()

    for order in orders_week:
        products_week.update(order.products.all())

    for order in orders_month:
        products_month.update(order.products.all())

    for order in orders_year:
        products_year.update(order.products.all())

    context = {
        'customer': customer,
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year,
    }

    return render(request, 'ordered_products_sort.html', context)