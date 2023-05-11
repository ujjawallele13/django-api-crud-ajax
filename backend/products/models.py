from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    introduction_date = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.product_name