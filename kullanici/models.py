from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Hesap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=11)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    

