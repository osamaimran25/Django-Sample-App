from django.urls import path
from petapp.views import *


urlpatterns = [

    ############ Cat CRUD ###############
    path('createcat', create_cat),
    path('updatecat/<int:pk>', update_cat),
    path('deletecat/<int:pk>', delete_cat),
    path('getcat/<int:pk>', get_cat),
    path('listcat', list_cat),
    
    ############ Dog CRUD ###############
    path('createdog', create_dog),
    path('updatedog/<int:pk>', update_dog),
    path('deletedog/<int:pk>', delete_dog),
    path('getdog/<int:pk>', get_dog),
    path('listdog', list_dog),
    
    ##########################
    ######### Login ##########
    #########################
    path('login', login),

]
