from django.db import models
from ..tasks.models import Task
from ..type.models import Type


class Event(models.Model):
    """
    Модель списка событий
    """
    name = models.CharField(max_length=256)
    picture = models.ImageField(upload_to='uploads/picture/')
    description = models.TextField()
    datebegin = models.DateTimeField()
    dateend = models.DateTimeField()
    # Отношения
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    type = models.OneToOneField(Type, on_delete=models.CASCADE)
