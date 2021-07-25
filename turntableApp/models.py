from django.db import models
from datetime import date
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class User_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         
    name = models.CharField(max_length=255,blank=True,null=False)      
    time = models.DateTimeField(auto_now=True)                          

    def __str__(self):
        return self.uid
# Create your models here.
class Winner_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         
    prize = models.CharField(max_length=255,blank=True,null=False) 
    name = models.CharField(max_length=255,blank=True,null=False)   
    phone = models.CharField(max_length=255,blank=True,null=False) 
    address = models.CharField(max_length=255,blank=True,null=False)   
    time = models.DateTimeField(auto_now=True)      
    def __str__(self):
        return self.uid
class Prize_Rate(models.Model):
    index = models.CharField(max_length=50,null=False,default='')         
    prize = models.CharField(max_length=255,blank=True,null=False) 
    rate = models.CharField(max_length=255,blank=True,null=False)   
    left = models.CharField(max_length=255,blank=True,null=False) 
    today = models.DateField(default=date.today)
    def __str__(self):
        return self.index
class Userdemo_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         
    time = models.DateTimeField(auto_now=True)                          
    def __str__(self):
        return self.uid
class claire_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         
    time = models.DateTimeField(auto_now=True)                          
    def __str__(self):
        return self.uid
class scratchDemo_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         
    time = models.DateTimeField(auto_now=True)                          
    def __str__(self):
        return self.uid
class hui_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')   
    prize = models.CharField(max_length=255,blank=True,null=False)       
    time = models.DateTimeField(auto_now=True)                          
    def __str__(self):
        return self.uid
class slot_info(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')   
    score = models.CharField(max_length=255,blank=True,null=False)       
    invite = models.CharField(max_length=255,blank=True,null=False)                         
    def __str__(self):
        return self.uid
class wen_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')   
    prize = models.CharField(max_length=255,blank=True,null=False)       
    time = models.DateTimeField(auto_now=True)                          
    def __str__(self):
        return self.uid
class snake_Player(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')
    name = models.CharField(max_length=50,null=False,default='')
    picture = models.CharField(max_length=100,null=False,default='')
    highscore = models.IntegerField()
    prize = models.CharField(max_length=500,null=False,default='')          
    time = models.DateTimeField(auto_now=True)                          
    def __str__(self):
        return self.uid
class heysongUid(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.uid
class HeysongScratch_User_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         
    name = models.CharField(max_length=255,blank=True,null=False)      
    time = models.DateTimeField(auto_now=True)                          

    def __str__(self):
        return self.uid
# Create your models here.
class HeysongScratch_Winner_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         
    prize = models.CharField(max_length=255,blank=True,null=False) 
    name = models.CharField(max_length=255,blank=True,null=False)   
    phone = models.CharField(max_length=255,blank=True,null=False) 
    email = models.CharField(max_length=255,blank=True,null=False) 
    address = models.CharField(max_length=255,blank=True,null=False)   
    time = models.DateTimeField(auto_now=True)      
    def __str__(self):
        return self.uid
class HeysongScratch_Prize_Rate(models.Model):
    index = models.CharField(max_length=50,null=False,default='')         
    prize = models.CharField(max_length=255,blank=True,null=False) 
    rate = models.CharField(max_length=255,blank=True,null=False)   
    left = models.CharField(max_length=255,blank=True,null=False) 
    today = models.DateField(default=date.today)
    def __str__(self):
        return self.index
class Traveltobuys_User_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         
    name = models.CharField(max_length=255,blank=True,null=False)      
    time = models.DateTimeField(auto_now=True)                          

    def __str__(self):
        return self.uid
# Create your models here.
class Traveltobuys_Winner_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         
    prize = models.CharField(max_length=255,blank=True,null=False) 
    name = models.CharField(max_length=255,blank=True,null=False)   
    phone = models.CharField(max_length=255,blank=True,null=False) 
    email = models.CharField(max_length=255,blank=True,null=False) 
    address = models.CharField(max_length=255,blank=True,null=False)   
    time = models.DateTimeField(auto_now=True)      
    def __str__(self):
        return self.uid
class Traveltobuys_Prize_Rate(models.Model):
    index = models.CharField(max_length=50,null=False,default='')         
    prize = models.CharField(max_length=255,blank=True,null=False) 
    rate = models.CharField(max_length=255,blank=True,null=False)   
    left = models.CharField(max_length=255,blank=True,null=False) 
    today = models.DateField(default=date.today)
    def __str__(self):
        return self.index
class jie_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')   
    prize = models.CharField(max_length=255,blank=True,null=False)       
    time = models.DateTimeField(auto_now=True)                          
    def __str__(self):
        return self.uid
class pei_Done(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')   
    prize = models.CharField(max_length=255,blank=True,null=False)       
    time = models.DateTimeField(auto_now=True)                          
    def __str__(self):
        return self.uid