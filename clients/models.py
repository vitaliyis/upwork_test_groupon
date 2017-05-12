from django.db import models
from orders.models import Order


class Client(models.Model):
    first_name = models.CharField(max_length=256, blank=False)
    last_name = models.CharField(max_length=256, blank=False)
    country = models.CharField(max_length=128, blank=False)
    city = models.CharField(max_length=128, blank=False)
    email = models.EmailField(blank=False)
    phone1 = models.CharField(max_length=128, blank=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class PrivateRoom(models.Model):
    client = models.ForeignKey(Client)
    order = models.ForeignKey(Order)