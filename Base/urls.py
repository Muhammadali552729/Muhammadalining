from django.urls import path
from .views import  *


urlpatterns = [
    path('', home, name='home'),
    path('detail/', detail, name='detail'),
    path('info/', info, name='info'),
    path('avto-bozor/', avto_bozor, name='avto-bozor'),
    path('index/', index, name='index'),
]