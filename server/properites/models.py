from django.db import models
from authentication.models import User
from address.models import Province, District, LocalLevel, LocalArea


class PropertyType(models.Model):
    property_type = models.CharField(max_length=200)


class PropertyImage(models.Model):
    image = models.ImageField()


class PropertyPrice(models.Model):
    amount = models.DecimalField(decimal_places=2,max_digits=10)
    updated_at = models.DateTimeField(auto_now_add=True)


class PropertyLocation(models.Model):
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    local_level = models.ForeignKey(LocalLevel, on_delete=models.DO_NOTHING)
    local_area = models.ForeignKey(LocalArea, on_delete=models.DO_NOTHING)
    remarks = models.TextField(blank=True)




class PropertyStatus(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    


class Property(models.Model):
    property_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    property_name = models.CharField(max_length=200)
    property_description = models.TextField()
    property_type = models.ForeignKey(PropertyType, on_delete=models.DO_NOTHING)
    no_bedrooms = models.IntegerField()
    property_image = models.ManyToManyField(PropertyImage)
    property_price = models.ManyToManyField(PropertyPrice)
    property_location = models.OneToOneField(PropertyLocation, on_delete=models.DO_NOTHING)
    property_status = models.ManyToManyField(PropertyStatus)


    