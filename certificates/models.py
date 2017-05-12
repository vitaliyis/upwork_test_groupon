from django.db import models


class CertificateCategory(models.Model):
    name = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return "%s" % (self.name)


class Certificate(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=True)
    category = models.ForeignKey(CertificateCategory)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField()
    price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_expiration = models.DateField()


    def __str__(self):
        return "%s %s " % (self.number, self.name)

