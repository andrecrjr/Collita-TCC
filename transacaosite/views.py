import json
from django.shortcuts import HttpResponse, render



def add_item_cart(request):
	return HttpResponse(request.session['cart'])

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