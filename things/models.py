from django.db import models
from django.db.models import Model

class Thing():
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()
