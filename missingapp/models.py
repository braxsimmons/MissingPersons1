from django.db import models
class Person (models.Model):
    dateMissing = models.DateField()
lastName = models.CharField(max_length=50)
firstName = models.CharField(max_length=50)
ageMissing = models.IntegerField()
    
# Create your models here.

# use class meta: db_table = "container" to link to container table on missingpersons.html