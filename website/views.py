from django.shortcuts import render
from apisite.models import *

# Create your views here.
def home(request):
    perfil = Profile.objects.all()
    return render(request,'index.html',{'usuarios':perfil})
