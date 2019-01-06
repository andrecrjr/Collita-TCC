from django.shortcuts import render
from apisite.models import *
from transacaosite.models import *
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
            return redirect(home())
        else:
            form = SignUpForm(request.POST or None)
    return render(request, 'signup.html', {'form': form})

def perfil(request,id):
    perfil = Inventario.objects.filter(usuario=id)
    items = Pedido.objects.filter(usuario_pedido=id)
    data_items = []
    if items:
        for item in items:
            data_items.append({
                'item_nome':item.item_pedido,
                'item_preco':item.item_pedido.valor_item
            })
    data_items.reverse()
    return render(request, 'perfil.html', {'dados':perfil,'items':data_items})
    

    


