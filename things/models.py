from django.db import models
from django.db.models import Model

class Thing:
    name = models.CharField()
    description = models.TextField()
    quantity = models.IntegerField()
