from django.contrib import admin
from .models import *

class CertificateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Certificate._meta.fields]

    class Meta:
        model = Certificate

admin.site.register(Certificate, CertificateAdmin)

class CertificateCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CertificateCategory._meta.fields]

    class Meta:
        model = CertificateCategory

admin.site.register(CertificateCategory, CertificateCategoryAdmin)