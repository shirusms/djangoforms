from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='upload',default='a.png')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
