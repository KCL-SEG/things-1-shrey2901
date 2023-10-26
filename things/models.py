from django.db.models import Model

class Thing(Model):
    name = models.CharField(max_length=30,unique = True, blank = False )
    description = models.CharField(max_length=120,blank =True)
    quantity = models.IntegerField()

    '''def __init__(self,name,description,quantity):
        self.name = name
        self.description = description
        self.quantity = quantity'''
