from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from transacaosite.models import *

def home(request):
    profile = []
    if request.user.is_authenticated:
        profile = Inventario.objects.all()
    return render(request, 'index.html', {'usuarios':profile})


def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    else:
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


def perfil(request, id_user):
    data_items = []
    try:        
        inventario = Inventario.objects.get(id=id_user)
        inventario_game = InventarioItemGame.objects.filter(usuario=inventario, quantidade__gt=0)
        for dados in inventario_game:
            item = Item.objects.get(id_item=dados.item_id)
            data_items.append({
                'item_nome':item,
                'item_quantidade':dados.quantidade,
                'item_img': item.imagem_item
            })
        perfil = Inventario.objects.filter(id=id_user)
        data_items.reverse()
    except:
        return redirect(home)
    return render(request, 'perfil.html', {'dados': perfil,'items':data_items})


def home_marketplace(request):
    items_estoque = []
    try:
        items = Item.objects.all()
        for item in items:
            items_estoque.append({
                'item_nome':item.nome_item,
                'item_preco':item.valor_item,
                'item_id': item.id_item,
                'item_img':item.imagem_item
            })
        items_estoque.reverse()
    except:
        items_estoque = None
    return render(request, 'marketplace.html', {'items':items_estoque})

def boleto_marketplace(request):
    boletos = []
    try:
        usuario = Inventario.objects.get(id=request.user.pk)
        for data in Transacao.objects.filter(usuario_transacao=usuario):
            boletos.append(data)
    except:
        boletos = None
    return render(request, 'boleto_wait.html', {'boletos':boletos})

def cart_marketplace(request):
    return render(request, 'marketplace_cart.html')