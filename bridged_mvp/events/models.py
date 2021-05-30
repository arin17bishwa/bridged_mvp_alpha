from django.db import models


# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=128)
    small_writeup = models.CharField(max_length=256)
    big_writeup = models.TextField(blank=True, null=True)
    link = models.URLField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return '{}({})'.format(self.title, self.start_time)
