from enum import auto
from django.db import models


class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=50 )
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()


    class Meta:
        ordering = ['created']