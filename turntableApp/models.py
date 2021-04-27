from django.db import models
from datetime import date

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