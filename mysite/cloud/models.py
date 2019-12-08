from django.db import models

# Create your models here.
class Review(models.Model):
    review1 = models.TextField()
    url = models.TextField()

class SReview(models.Model):
    review = models.TextField()
    url = models.TextField()
    
