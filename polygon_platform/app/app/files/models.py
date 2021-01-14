from django.db import models


class Files(models.Model):
    """
    Модель файлов, которые могут быть прикреплены к заданиям
    """
    name = models.CharField(max_length=256)
    picture = models.FileField(upload_to='uploads/files/')
    description = models.TextField()
