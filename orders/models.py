from django.db import models
from clients.models import Client
from certificates.models import Certificate


class Order(models.Model):
    client = models.ForeignKey(Client, blank=False, null=True)
    quantity_certificate = models.IntegerField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


class CertificateInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    certificate = models.ForeignKey(Certificate, blank=True, null=True, default=None)