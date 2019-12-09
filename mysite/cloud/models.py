from django.db import models

# Create your models here.
class Review(models.Model):
    review1 = models.TextField()
    url = models.TextField()

class SReview(models.Model):
    review = models.TextField()
    url = models.TextField()

class Rank(models.Model):
    pname = models.CharField(max_length=50)

class Shopping(models.Model):
    img = models.TextField()
    title = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.CharField(max_length=100)
