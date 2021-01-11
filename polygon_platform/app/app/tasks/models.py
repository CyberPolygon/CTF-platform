from django.db import models
from polygon_platform.app.app.files.models import Files
from polygon_platform.app.app.type.models import Type


class Task(models.Model):
    """
    Модель задания
    """
    name = models.CharField(max_length=256)
    flag = models.CharField(max_length=256)
    picture = models.ImageField(upload_to='uploads/picture/')
    description = models.TextField()
    # Отношения
    files = models.ForeignKey(Files, on_delete=models.CASCADE)
    type = models.OneToOneField(Type, on_delete=models.CASCADE)
