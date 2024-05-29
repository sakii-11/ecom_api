from django.db import models
# Create your models here.

class Product(models.Model):
  title = models.CharField(max_length=100, blank=False, null= False)
  image = models.URLField()
  price = models.DecimalField(max_digits= 10, decimal_places= 3)
  description = models.TextField()
  popularity = models.IntegerField()
  
  def __str__(self):
    return self.title