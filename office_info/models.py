from django.db import models
from django.db.models.fields import CharField

class Office(models.Model):
    title = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    address_line_3 = models.CharField(max_length=100, blank=True)
    address_line_4 = models.CharField(max_length=100, blank=True)
    postal_zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    openweathermap_id = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100)
    image = models.ImageField(upload_to='huddl/images/')