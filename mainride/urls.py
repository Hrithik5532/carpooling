from django.urls import path
from .views import *
urlpatterns = [
    path('createride/',createride,name="createride"),
    path('bookride/',bookride,name='bookride'),
    path('getroute/',find_route,name='getroute')
]