from django.db import models


class Library(models.Model):
    day = models.CharField(max_length=70, blank=False, default='')
    timings = models.CharField(max_length=200,blank=False, default='')
    