from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim
    
class AltKategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim
    

class Tek(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim
    

class Urun(models.Model):
    satici = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null = True)
    altkategori = models.ManyToManyField(AltKategori)
    seriNo = models.OneToOneField(Tek, on_delete=models.CASCADE, null=True, blank=True)
    isim = models.CharField(max_length=100)
    aciklama = models.TextField(max_length=1000)
    fiyat = models.IntegerField()
    resim = models.FileField(upload_to= 'urunler/') #* file input

    def __str__(self):
        return self.isim
    

class Sepet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE, null=True)
    adet = models.IntegerField()
    toplamFiyat = models.IntegerField()
    odendiMi = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username