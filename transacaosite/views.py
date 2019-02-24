import json
from django.shortcuts import HttpResponse, render


def add_item_cart(request):
	if request.is_ajax():
		if request.method == 'POST':
			valor = json.loads(request.body.decode('utf-8'))
			print(valor['data'])
	return HttpResponse('ok')

def session_id(request):
    if request.user.is_authenticated:
        response_data = {}
        new_id = 'valor'
        response_data['session_id'] = new_id
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def delete_cart(request):
	if request.session['cart']:
		del request.session['cart']
		return HttpResponse('just vanished')
	else:
		return HttpResponse('apagado')