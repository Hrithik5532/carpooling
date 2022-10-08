from django.shortcuts import render
from django.http import HttpResponse  ,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from usercreationApp.models import docverifyModel, usercreate  
from .forms import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .token import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
# Create your views here.



  
def signup(request): 
    if request.method == 'POST':  
        form = SignupForm(request.POST)  
        if form.is_valid():  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save() 

            return render(request, 'login.html')  
        else:
            return HttpResponse(form.errors)  
    
            # current_site = get_current_site(request)  
            # mail_subject = 'Activation link has been sent to your email id'  
            # message = render_to_string('acc_active_email.html', {  
            #     'user': user,  
            #     'domain': current_site.domain,  
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
            #     'token':account_activation_token.make_token(user),  
            # })  
            # to_email = form.cleaned_data.get('email')  
            # email = EmailMessage(  
            #             mail_subject, message, to=[to_email]  
            # )  
            # email.send()  
    else:  
        form = SignupForm()  
    return render(request, 'signup.html')  

def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        user= usercreate.objects.get(email=email,password=password)

        # 
        return HttpResponseRedirect(reverse('userprofile', args=[user.id]))
        # except:
        #     return HttpResponse('error')
    
    return render(request,'login.html')


def userprofile(request,id):
    user = usercreate.objects.get(id=id)
    try:
        doc = docverifyModel.objects.get(did = id)
    except :
        doc = None
    return render(request,'profile.html',{'user':user,'doc':doc})


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  