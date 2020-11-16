from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def upload(request):
    print(request.POST.dict())
    return JsonResponse({
  "code": 0
  ,"msg": ""
  ,"data": {
    "src": "http://cdn.layui.com/123.jpg"
  }
}   ,safe=True)