import json
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_item_cart(request):
	if request.method == 'POST':
		cart_session = request.session[request.user.username]
		cart_session.append(json.loads(request.body.decode('utf-8')))
		request.session[request.user.username] = cart_session
		print(request.session[request.user.username])
		return HttpResponse('ok')

def list_items(request):
	request.session.get(request.user.username)
	return HttpResponse(json.dumps(request.session[request.user.username]))


def delete_cart(request):
	valor = request.session.get(request.user.username)
	if valor:
		valor.clear()
		return HttpResponse('apagado com sucesso')

	return HttpResponse('nada')