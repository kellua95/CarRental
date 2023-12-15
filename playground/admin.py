from django.contrib import admin

from .models import Cars, Collection, Custoumer
# Register your models here.

admin.site.register(Cars)
admin.site.register(Collection)
admin.site.register(Custoumer)