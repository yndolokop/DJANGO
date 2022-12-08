from django.db import models


# Create your models here.
class Predict(models.Model):
    set = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.set


class Result(models.Model):
    # Id уже не нужно указывать как во Фласк. Появится сам.
    date = models.CharField(max_length=32)
    n1 = models.PositiveIntegerField()
    n2 = models.PositiveIntegerField()
    n3 = models.PositiveIntegerField()
    n4 = models.PositiveIntegerField()
    n5 = models.PositiveIntegerField()
    s1 = models.PositiveIntegerField()
    s2 = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.date


class User(models.Model):
    name = models.CharField(max_length=32, unique=True)
    email = models. EmailField(max_length=254)
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
