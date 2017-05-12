from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class CertificateInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CertificateInOrder._meta.fields]

    class Meta:
        model = CertificateInOrder

admin.site.register(CertificateInOrder, CertificateInOrderAdmin)