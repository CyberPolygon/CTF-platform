from django.db import models
from polygon_platform.app.app.tasks.models import Task


class Event(models.Model):
    """
    Модель списка событий
    """
    name = models.CharField(max_length=256)
    picture = models.ImageField(upload_to='uploads/picture/')
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    datebegin = models.DateTimeField()
    dateend = models.DateTimeField()
