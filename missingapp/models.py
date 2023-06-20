from django.db import models

class Person (models.Model):
    dateMissing = models.DateField(blank=True)
    lastName = models.CharField(max_length=50, default='Unknown')
    firstName = models.CharField(max_length=50, default='Unknown')
    ageMissing = models.IntegerField(default=1)
    city = models.CharField(max_length=50, default='Unknown')
    state = models.CharField(max_length=50, default='Unknown')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    race  = models.CharField(max_length=50, default='Unknown')

    def __str__(self):
            return self.firstName
# Create your models here.

# use class meta: db_table = "container" to link to container table on missingpersons.html
