import uuid
from django.db import models

# Create your models here.

class usercreate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # username=models.CharField(max_length=10,unique=True)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)

    add= models.TextField()
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=7)
    password = models.CharField(max_length=10)
    cpssword=models.CharField(max_length=10)
    active = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)



class docverifyModel(models.Model):
    def upload_to(instance,filename):
            
        return 'panimg/%s.jpg' %(instance.did.id)

    did = models.OneToOneField(usercreate,on_delete=models.CASCADE)
    panimg=models.ImageField(upload_to =upload_to)
    aadharimg = models.ImageField(upload_to=upload_to)
    drivinglicimg= models.ImageField(upload_to="drivinglicimg/",null=True,blank=True)
    panno=models.CharField(max_length=10)
    aadharno = models.CharField(max_length=12)
    drivinglicno=models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return str(self.did.id)
        
    