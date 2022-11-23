from django.db import models
from django.conf import settings


class Provider(models.Model):
    company_name = models.CharField(max_length=100)
    founder = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    information = models.TextField(blank=True, null=True)


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    provider = models.OneToOneField(Provider, settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country_of_production = models.CharField(max_length=50)
    price = models.FloatField()
    characteristics = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.brand

