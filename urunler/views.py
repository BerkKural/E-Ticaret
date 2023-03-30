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