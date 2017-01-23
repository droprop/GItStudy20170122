from django.db import models

# Create your models here.

class Talk (models.Model):
    """トーク"""
    name = models.CharField('NAME', max_length=255)
    content = models.CharField('CONTENT', max_length=255)
    weight = models.IntegerField('WEIGHT')

    def __str__(self):
        return self.content
