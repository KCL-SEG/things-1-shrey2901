from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(unique =True, max_length= 30,blank=False)
    description = models.CharField(max_length= 120,blank=True)
    quantity = models.IntegerField(validators=
    [MinValueValidator(0), MaxValueValidator(100)])
