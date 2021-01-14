from django.db import models


class Type(models.Model):
    """
    Модель типов сущеностей в системе
    """
    type = models.IntegerField()
    subtype = models.IntegerField()
    name = models.CharField(max_length=256)
