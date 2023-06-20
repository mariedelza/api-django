from django.shortcuts import render
import json
from django.http import JsonResponse


# Create your views here.

def api_view(request, *args, **kwargs):
    data={
        'name':'marie',
        'language':'python'
    }
    # print(request.body)
    # data=json.loads(request.body)
    # print(data)
    # data['headers']=dict(request.headers)
    # data['params']=dict(request.GET)
    # data['post-data']=dict(request.POST)
    # print(request.headers)
    # data['content_type']=request.content_type
    return JsonResponse(data)