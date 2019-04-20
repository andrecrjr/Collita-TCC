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
        pedidos = Transacao.objects.filter(usuario_transacao=inventario)
        for data in pedidos:
            for itens in data.item_transacao.all():
                if itens.quantidade != 0:
                    data_items.append({
                            'item_nome':itens.item,
                            'item_quantidade':itens.quantidade,
                            'item_img':itens.item.imagem_item
                    })
        perfil = Inventario.objects.filter(id=id_user)
        data_items.reverse()
    except:
        perfil = None
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
    try:
        usuario = Inventario.objects.get(id=request.user.pk)
        boletos = []
        for data in Transacao.objects.filter(usuario_transacao=usuario):
            boletos.append(data)
        return render(request, 'boleto_wait.html', {'boletos':boletos})
    except:
        return HttpResponse('problem')
