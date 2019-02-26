import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_item_cart(request):
	usuario = request.user.username
	if request.method == 'POST':
		print(usuario)
		cart_session = request.session.get(usuario, [])
		cart_session.append(json.loads(request.body.decode('utf-8')))
		request.session[usuario] = cart_session
		print(request.session[usuario])
		return HttpResponse('ok')
	else:
		return HttpResponse('erro 404')


def list_items(request):

	data = request.session.get(request.user.username)
	return HttpResponse(json.dumps(data), content_type="application/json")

'''
def delete_item(request):
	cart = request.session.get(request.user.username)
	del data[item_id]
	return HttpResponse()
'''

def delete_cart(request):
	data = request.session.get(request.user.username)
	if data:
		data.clear()
		request.session.modified = True
		return HttpResponse('apagado com sucesso')
	else:
		return HttpResponse('nada')