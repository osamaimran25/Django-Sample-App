from django.http import HttpResponse
from django.http import JsonResponse
from functools import wraps
import jwt
import petapp.views as config

SECRET_KEY = "cbtestdone"


def token_required(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        try:
            token = request.GET['token']
        except:
            return JsonResponse({'Error': "Token is missing"}, status=403)
        try:
            jwt.decode(token, SECRET_KEY)
        except:
            return JsonResponse({'Error': "Invalid Token"}, status=403)

        return f(request, *args, **kwargs)
    return decorated
