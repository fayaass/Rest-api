from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *

# Create your views here.

# def sample(req):
#     d={'name':'fayas','age':22}
#     return JsonResponse(d)


def user_def_serializer(req):
    if req.method=='GET':
        data=student.objects.all()
        d=user_serializers(data,many=True)
        return JsonResponse(d.data,safe=False)