from django.shortcuts import render
from transacaosite.models import *
from django.shortcuts import redirect
from .forms import *

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
            return redirect(home)
        else:
            form = SignUpForm(request.POST or None)
    return render(request, 'signup.html', {'form': form})


def perfil(request, id_user):
    inventario = Inventario.objects.filter(id=id_user)
    pedidos = Inventario.objects.get(id=id_user)
    data_items = []
    for item in pedidos.transacao_inventario.all():
        data_items.append({
                'item_nome':item.item_comprado,
                'item_preco':item.item_comprado.valor_item
        })
    data_items.reverse()
    return render(request, 'perfil.html', {'dados':inventario, 'items':data_items})


def home_marketplace(request):
    items = Item.objects.all()
    items_estoque = []
    for item in items:
        items_estoque.append({
            'item_nome':item.nome_item,
            'item_preco':item.valor_item,
            'item_id': item.id,
            'item_img':item.imagem_item
        })

    return render(request, 'marketplace.html', {'items':items_estoque})

def marketplace_checkout(request, item_id):
    user = []
    '''
    from transacaosite.helper import gerar_boleto
    boleto_final = gerar_boleto(item_id)
    '''
    return render(request, 'checkout.html')
