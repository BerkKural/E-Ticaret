from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
from .forms import *

# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    kategoriler = Kategori.objects.all()
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(
            Q(isim__icontains = search) |
            Q(aciklama__icontains = search) |
            Q(kategori__isim__icontains = search)
        )
    if request.method == 'POST':
        urunId = request.POST['urunId']
        adet = request.POST['adet']
        urun = Urun.objects.get(id = urunId)
        if Sepet.objects.filter(user = request.user, urun = urun, odendiMi = False).exists():
            sepet = Sepet.objects.get(user = request.user, urun = urun, odendiMi = False)
            sepet.adet +=int(adet)
            sepet.toplamFiyat = sepet.urun.fiyat * sepet.adet
            sepet.save()
            messages.success(request, 'Sepete ürün eklendi')
            return redirect('index')
        else:
            sepet = Sepet.objects.create(
                user = request.user,
                urun = urun,
                adet = adet,
                toplamFiyat = urun.fiyat * int(adet)
            )
            sepet.save()
            messages.success(request, 'Sepete eklendi')
            return redirect('index')

    context = {
        'product': urunler,
        'search' : search,
        'kategoriler' : kategoriler,
    }
    return render(request, 'index.html', context)

def urun(request, urunId):
    urun = Urun.objects.get(id = urunId)
    context = {
        'urun': urun
    }
    return render(request, 'urun.html', context)

def olustur(request):
    form = UrunForm()
    if request.method == 'POST':
        form = UrunForm(request.POST, request.FILES)
        if form.is_valid():
            yeniUrun = form.save(commit=False)
            yeniUrun.satici = request.user
            yeniUrun.save()
            messages.success(request, 'Ürün Oluşturuldu!')
            return redirect('index')
        
    context = {
        'form':form
    }
    return render(request, 'olustur.html', context)

def sepet(request):
    sepet = Sepet.objects.filter(user = request.user, odendiMi = False)
    context = {
        'sepet':sepet
    }
    return render(request, 'sepet.html', context)