
from django.urls import path
from .views import *
urlpatterns = [
    path('signup',signup,name='signup'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  
    path('userlogin',userlogin,name='userlogin'),    
    path('userprofile/(?P<id>[-\w]+)/$',userprofile,name='userprofile'),
]