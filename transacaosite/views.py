import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_item_cart(request):
	if request.method == 'POST':
		usuario = request.user.username
		cart_session = request.session.get(usuario, [])
		cart_session.append(json.loads(request.body))
		request.session[usuario] = cart_session
		return HttpResponse('ok')
	else:
		return HttpResponse('erro 404')


def list_items(request):
	data = request.session.get(request.user.username)
	return HttpResponse(json.dumps(data), content_type="application/json")

'''
def delete_item(request, cart_id):
	cart = request.session.get(request.user.username)
	del cart[item_id]
	request.session.modified = True
	return HttpResponse()
'''

def delete_cart(request):
	if request.method == 'GET':
		data = request.session.get(request.user.username)
		if data:
			data.clear()
			request.session.modified = True
			return HttpResponse('apagado com sucesso')
		else:
			return HttpResponse('nada')