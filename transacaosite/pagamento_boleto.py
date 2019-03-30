
def wait_boleto(request):
    if request.method == 'GET':
        itens = request.session.get('boleto' + request.user.username, [])
        print(itens)