
def wait_boleto(request):
    if request.method == 'GET':
        itens = request.session.get('boleto_' + request.user.username, [])
        print(itens)