import requests
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from carpooling import settings


# Create your views here.
def createride(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'cancel' in request.POST:
                request.session.flush()
                return redirect('mapview')
            
            if 'confirm' in request.POST:
                no_seats= request.POST.get('no_seats')
                price= request.POST.get('price')
                yr= request.POST.get('yr')
                car= request.POST.get('car')
                model= request.POST.get('model')
                fueltype= request.POST.get('fueltype')
                insured= request.POST.get('insured')

                if insured == None:
                    
                    return redirect('mapview')

                user =request.user
                ride = createRideLoc.objects.create(did = user,from_address=request.session['createride']['from_address'],to_address=request.session['createride']['to_address'],from_lat=request.session['createride']['from_lat'],from_long=request.session['createride']['from_long'],to_lat=request.session['createride']['to_lat'],
                                                    to_long=request.session['createride']['to_long'],date=request.session['createride']['date'],time=request.session['createride']['time'],price=price,yr=yr,car=car,model=model,fueltype=fueltype,no_of_seats=no_seats)

                ride.save()
                return HttpResponse('Ride Saved')
    return redirect('userlogin')
def bookride(request):
    return HttpResponse()


def find_route(request):


    return redirect('mapview')