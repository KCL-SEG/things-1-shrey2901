from django.db import models
from django.db.models import Model

class Thing():
    def __init__(self):
        name = models.CharField(max_length=30,unique = True, blank = False )
        description = models.CharField(max_length=120,blank =True)
        quantity = models.IntegerField(min_value=0, max_value=100)
