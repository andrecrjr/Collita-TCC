from django.shortcuts import render
from apisite.models import *
from transacaosite.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth import authenticate, login


def home(request):
    profile = []
    if request.user.is_authenticated:
        profile = Inventario.objects.all()
    return render(request, 'index.html', {'usuarios':profile})

def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            form.save()
            return redirect(perfil)
        else:
            form = SignUpForm(request.POST or None)
    return render(request, 'signup.html', {'form': form})

def perfil(request, id_user):
    inventario = Inventario.objects.filter(id=id_user)
    pedidos = Inventario.objects.get(id=id_user)
    data_items = []
    for item in pedidos.inventario_pedido.all():
        data_items.append({
                'item_nome':item.item_pedido,
                'item_preco':item.item_pedido.valor_item
        })
    data_items.reverse()
    return render(request, 'perfil.html', {'dados':inventario, 'items':data_items})

