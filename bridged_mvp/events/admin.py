from django.contrib import admin
from .models import Event,Testimonial
# Register your models here.

admin.site.register((Event,Testimonial))
