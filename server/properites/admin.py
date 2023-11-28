from django.contrib import admin

from .models import Property, PropertyImage, PropertyLocation, PropertyPrice, PropertyStatus, PropertyType

# Register your models here.

admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(PropertyLocation)
admin.site.register(PropertyPrice)
admin.site.register(PropertyStatus)
admin.site.register(PropertyType)