from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def kayit(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kullanıcı Oluşturuldu!')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def giris(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Yapıldı!')
            return redirect('index')
        else:
            messages.warning(request, 'Kullanıcı Adı / Şifre Hatalı!')
            return redirect('login')
    return render(request, 'login.html')

def cikis(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı!')
    return redirect('index')