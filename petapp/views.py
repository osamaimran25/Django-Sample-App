from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from datetime import datetime
from .models import *

# Create your views here.


@csrf_exempt
def create_cat(request):

    if request.method != "POST":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    request_data = json.loads(request.body)

    cat_name                = request_data['cat_name']
    cat_date_of_birth       = request_data['cat_date_of_birth']
    owner_id                = request_data['owner_id']

    try:
        owner = Owner.objects.get(id=int(owner_id))
    except:
        return JsonResponse({"Error": "No Owner Exist"}, status=404)

    cat                     = Cat()
    cat.name                = cat_name
    cat.date_of_birth       = cat_date_of_birth
    cat.owner               = owner
    cat.save()

    return JsonResponse({"Success": "Record Saved", "id": str(cat.id)})


@csrf_exempt
def update_cat(request, pk):

    if request.method != "PUT":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    request_data = json.loads(request.body)

    cat_name = request_data['cat_name']
    cat_date_of_birth = request_data['cat_date_of_birth']
    owner_id = request_data['owner_id']

    try:
        cat = Cat.objects.get(id=pk)
    except:
        return JsonResponse({"Error": "No Cat Exist"}, status=404)

    try:
        owner = Owner.objects.get(id=int(owner_id))
    except:
        return JsonResponse({"Error": "No Owner Exist"}, status=404)

    cat = Cat.objects.filter(id=pk).update(name = cat_name,date_of_birth = cat_date_of_birth,owner = owner)

    return JsonResponse({"Success": "Record Updated"})



@csrf_exempt
def get_cat(request, pk):

    if request.method != "GET":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    
    cat = Cat.objects.filter(id=pk).values('name','date_of_birth','owner_id')

    if cat:
        cat = cat[0]
        cat['owner_id']  = str(cat['owner_id'])
    else:
        return JsonResponse({"Error": "No Cat Exist"}, status=404)



    return JsonResponse(cat,safe=False)

@csrf_exempt
def list_cat(request):

    if request.method != "GET":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    
    list_of_cat = []

    cats = Cat.objects.filter().values('name','date_of_birth','owner_id')
    
    if cat:
        for cat in cats    
        cat['owner_id']  = str(cat['owner_id'])
    else:
        return JsonResponse({"Error": "No Cat Exist"}, status=404)



    return JsonResponse(cat,safe=False)

