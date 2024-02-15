from django.core.management.base import BaseCommand
from store_app.models import Customer


class Command(BaseCommand):
    help = "Read all customers"

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()

        for customer in customers:
            self.stdout.write(str(customer))
