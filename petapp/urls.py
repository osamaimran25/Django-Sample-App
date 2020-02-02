from django.urls import path
from petapp.views import *


urlpatterns = [
    path('createcat', create_cat),
    path('updatecat/<int:pk>', update_cat),
    path('getcat/<int:pk>', get_cat),
]
