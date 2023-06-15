from django.db import models

class Person (models.Model):
    dateMissing = models.CharField(max_length=50, default='name date')
    lastName = models.CharField(max_length=50, default='name unknown')
    firstName = models.CharField(max_length=50, default='name unknown')
    ageMissing = models.IntegerField(default=1)
    city = models.CharField(max_length=50, default='city unknown')
    state = models.CharField(max_length=50, default='state unknown')
    gender = models.CharField(max_length=50, default='gender unknown (M or F only)')
    race  = models.CharField(max_length=50, default='race unknown')
# Create your models here.

# use class meta: db_table = "container" to link to container table on missingpersons.html
