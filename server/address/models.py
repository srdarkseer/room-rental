from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=10)

class District(models.Model):
    name = models.CharField(max_length=20)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)

class LocalLevel(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)

class LocalArea(models.Model):
    name = models.CharField(max_length=50)
    local_level = models.ForeignKey(LocalLevel, on_delete=models.DO_NOTHING)

