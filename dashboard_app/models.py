from django.contrib.auth.models import User
from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Subscription(models.Model):
    app = models.OneToOneField(App, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

