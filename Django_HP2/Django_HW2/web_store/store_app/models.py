from django.db import models

# Create your models here.


class Customer(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    user_phone = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer:{self.username}, email:{self.email}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_of_addition = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.product_name}, price: {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order: {self.id} - {self.customer.name}'
