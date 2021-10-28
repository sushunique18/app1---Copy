from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    weight =models.DecimalField(max_digits=6,decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


