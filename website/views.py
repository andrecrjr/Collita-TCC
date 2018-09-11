from django.shortcuts import render
from apisite.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    perfil = Profile.objects.all()
    return render(request,'index.html',{'usuarios':perfil})

def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            form.save()
            return redirect(home)
        else:
            form = SignUpForm(request.POST or None)
    return render(request, 'signup.html', {'form': form})

def perfil(request,id):
    perfil = Profile.objects.filter(id=id)
    print(perfil)
    return render(request, 'perfil.html', {'dados':perfil})
