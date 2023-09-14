from django.db import models


class my_apps(models.Model):

    date = models.DateField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',)

