from django.contrib import admin
from .models import Province, District, LocalLevel, LocalArea

# Register your models here.

admin.site.register(Province)
admin.site.register(District)
admin.site.register(LocalLevel)
admin.site.register(LocalArea)
