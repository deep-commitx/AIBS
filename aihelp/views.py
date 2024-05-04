from django.shortcuts import render
# from .chat_gpt import get_chat_response
from django.http import HttpResponse
import json
from .chat import get_chat_response

# Create your views here.
# 
# def index(request):
    # return render(request, "index.html")
# 
# 
# def chat_gpt(request):
    # 
    # response = get_chat_response(request.GET.get('prompt'))
    # print(response)
# 
    # return HttpResponse(json.dumps(response), content_type='application/json')

class AiHelp():
    def index(request):
        return render(request, "index.html")


    def chat_gpt(request):
        response = get_chat_response(request.GET.get('prompt'))
        # print(response)
        return HttpResponse(json.dumps(response), content_type='application/json')