from django.db import models
from datetime import datetime

# Create your models here.


def upload_location(instance, filename, **kwargs):
    file_path = 'content/{name}/{time}-{filename}'.format(
        time=str(datetime.now().strftime("%H%M%S%f")),
        name=instance.name,
        filename=filename
    )
    print(file_path)
    return file_path


class Content(models.Model):
    name = models.CharField(max_length=32)
    short_description=models.CharField(max_length=128)
    image = models.ImageField(upload_to=upload_location)

    def __str__(self):
        return '{}-{}...'.format(self.name,self.short_description[:15:1])
