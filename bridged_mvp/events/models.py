from django.db import models
from datetime import datetime

# Create your models here.


def upload_location(instance, filename, **kwargs):
    file_path = '{time}-{filename}'.format(
        time=str(datetime.now().strftime("%H%M%S%f")),
        filename=filename
    )
    print(file_path)
    return file_path


class Event(models.Model):
    title = models.CharField(max_length=128)
    small_writeup = models.CharField(max_length=256)
    big_writeup = models.TextField(blank=True, null=True)
    link = models.URLField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return '{}({})'.format(self.title, self.start_time)


class Testimonial(models.Model):
    name = models.CharField(max_length=32)
    about=models.CharField(max_length=128)
    testimonial=models.TextField()
    image = models.ImageField(upload_to=upload_location)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}....'.format(self.name,self.testimonial[:20:1])
