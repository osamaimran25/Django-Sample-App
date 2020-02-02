from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
import json
import datetime
from .models import *
import base64

from .toekn_decorater import token_required

SECRET_KEY = "cbtestdone"
#############################
#### Cat CRUD Opereations ###
############################
@token_required
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

@token_required
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

@token_required
@csrf_exempt
def delete_cat(request, pk):

    if request.method != "DELETE":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    
    try:
        cat = Cat.objects.get(id=pk)
        cat.delete()
    except:
        return JsonResponse({"Error": "No Cat Exist"}, status=404)


    return JsonResponse({"Success":"Cat Deleted...!"})

@token_required
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
@token_required
@csrf_exempt
def list_cat(request):

    if request.method != "GET":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    
    list_of_cat = []

    cats = Cat.objects.filter().values('name','date_of_birth','owner_id')
    
    if cats:
        for cat in cats:    
            cat['owner_id']  = str(cat['owner_id'])
            list_of_cat.append(cat)
    else:
        return JsonResponse({"Error": "No Cat Exist"}, status=404)

    return JsonResponse(list_of_cat,safe=False)


#############################
#### Dog CRUD Opereations ###
############################
@token_required
@csrf_exempt
def create_dog(request):

    if request.method != "POST":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    request_data = json.loads(request.body)

    dog_name                = request_data['dog_name']
    dog_date_of_birth       = request_data['dog_date_of_birth']
    owner_id                = request_data['owner_id']

    try:
        owner = Owner.objects.get(id=int(owner_id))
    except:
        return JsonResponse({"Error": "No Owner Exist"}, status=404)

    dog                     = Dog()
    dog.name                = dog_name
    dog.date_of_birth       = dog_date_of_birth
    dog.owner               = owner
    dog.save()

    return JsonResponse({"Success": "Record Saved", "id": str(dog.id)})

@token_required
@csrf_exempt
def update_dog(request, pk):

    if request.method != "PUT":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    request_data = json.loads(request.body)

    dog_name = request_data['dog_name']
    dog_date_of_birth = request_data['dog_date_of_birth']
    owner_id = request_data['owner_id']

    try:
        dog = Dog.objects.get(id=pk)
    except:
        return JsonResponse({"Error": "No dog Exist"}, status=404)

    try:
        owner = Owner.objects.get(id=int(owner_id))
    except:
        return JsonResponse({"Error": "No Owner Exist"}, status=404)

    dog = Dog.objects.filter(id=pk).update(name = dog_name,date_of_birth = dog_date_of_birth,owner = owner)

    return JsonResponse({"Success": "Record Updated"})

@token_required
@csrf_exempt
def delete_dog(request, pk):

    if request.method != "DELETE":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    
    try:
        dog = Dog.objects.get(id=pk)
        dog.delete()
    except:
        return JsonResponse({"Error": "No dog Exist"}, status=404)


    return JsonResponse({"Success":"Dog Deleted...!"})

@token_required
@csrf_exempt
def get_dog(request, pk):

    if request.method != "GET":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    
    dog = Dog.objects.filter(id=pk).values('name','date_of_birth','owner_id')

    if dog:
        dog = dog[0]
        dog['owner_id']  = str(dog['owner_id'])
    else:
        return JsonResponse({"Error": "No Dog Exist"}, status=404)



    return JsonResponse(dog,safe=False)
@token_required
@csrf_exempt
def list_dog(request):

    if request.method != "GET":
        return JsonResponse({"Error": "Unsupported Method"}, status=500)

    
    list_of_dog = []

    dogs = Dog.objects.filter().values('name','date_of_birth','owner_id')
    
    if dogs:
        for dog in dogs:    
            dog['owner_id']  = str(dog['owner_id'])
            list_of_dog.append(dog)
    else:
        return JsonResponse({"Error": "No Cat Exist"}, status=404)

    return JsonResponse(list_of_dog,safe=False)



@csrf_exempt
def login(request):
    auth =  request.META['HTTP_AUTHORIZATION']
    encoded_credentials = auth.split(' ')[1]  # Removes "Basic " to isolate credentials
    decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
    username = decoded_credentials[0]
    password = decoded_credentials[1]
    print("aaa",password)
    
    try:
        owner_credentials = Owner.objects.get(name=username,password=password)
        
    except :
        return JsonResponse({"Error":"No User Found"},status=404)
    
    if owner_credentials:
        token = jwt.encode({'user': owner_credentials.name,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=20)},SECRET_KEY)
        return JsonResponse({'token': token.decode('UTF-8')})

    return JsonResponse({"Error":"Could not Verify"},status=400)





