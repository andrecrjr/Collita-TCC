import json
from django.shortcuts import HttpResponse


def session_id(request):
    if request.user.is_authenticated:
        response_data = {}
        new_id = 'valor'
        response_data['session_id'] = new_id
        return HttpResponse(json.dumps(response_data), content_type="application/json")
