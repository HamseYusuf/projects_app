from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):

    status_choises = (
        ('new' , 'new'),
        ('inprogreess' , 'inprogress'),
        ('completed' , 'completed')

    )

    user = models.ForeignKey(User , on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    technology = models.CharField(max_length=100)
    developers = models.CharField(max_length=200)
    details = models.TextField()
    status = models.CharField(max_length=100 , choices=status_choises)

    def __str__(self):
        return self.title

