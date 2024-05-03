from django.db import models
from User.models import User


class Stadium(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=13, unique=True, null=False, blank=False)
    price_per_hour = models.FloatField(null=False, blank=False)
    description = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class StadiumImage(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    is_main = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "%s - %s" % (self.stadium, self.is_main)
