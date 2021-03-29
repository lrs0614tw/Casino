from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
import datetime
import json
from turntableApp.models import *

# Create your views here.
def index(request,day):
    uid = request.GET.get('uid','')
    return render(request,'index.html',locals())
def liff(request):
    finish=request.GET.get('finish','')
    return render(request,'liff.html',locals())
def game(request):
    uid = request.GET.get('uid','')
    today=datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    prize_object=Prize_Rate.objects.filter(today=today)
    prize_rate={}
    prize_left={}
    for i in prize_object:
        prize_rate[i.index]=i.rate
        prize_left[i.index]=i.left
    prize_rate2=json.dumps(prize_rate)
    prize_left2=json.dumps(prize_left)
    beenWin='0'
    if(Winner_Done.objects.filter(uid=uid).exists()):
        beenWin='1'
    if(User_Done.objects.filter(uid=uid,time__lt=tomorrow,time__gte=today).exists()==True):
        if(Winner_Done.objects.filter(uid=uid,time__lt=tomorrow,time__gte=today).exists()):
            return render(request,'gameAlready.html',locals())
        else:
            user=User_Done.objects.filter(uid=uid,time__lt=tomorrow,time__gte=today)
            prize=user[0].name
            if(prize!='明日再試！'):
                return render(request,'gameWin.html',locals()) 
            else:
                return render(request,'gameAlready.html',locals())
                
    elif(uid!=''):
        return render(request,'game.html',locals())
    else:
        return render(request,'gameAlready.html',locals())
@csrf_exempt
def gameDone(request):
    uid=request.POST['uid']
    pname=request.POST['pname']
    newLeft=request.POST['newLeft']
    index=request.POST['index']
    today=datetime.date.today()
    User_Done.objects.create(uid=uid,name=pname)
    Prize_Rate.objects.filter(index=index,today=today).update(left=newLeft)
    return HttpResponse("表單回傳成功") 
def gameForm(request):
    prize=request.GET.get('prize','')
    uid=request.GET.get('uid','')
    return render(request,'gameForm.html',locals())
@csrf_exempt
def formDone(request):
    name=request.POST['name']
    phone=request.POST['phone']
    address=request.POST['address']
    prize=request.POST['prize']
    uid=request.POST['uid']
    return render(request,'formDone.html',locals())
@csrf_exempt
def allDone(request):
    uid=request.POST['uid']
    prize=request.POST['prize']
    name=request.POST['name']
    phone=request.POST['phone']
    address=request.POST['address']
    Winner_Done.objects.create(uid=uid,prize=prize,name=name,phone=phone,address=address)
    return HttpResponse("表單回傳成功") 
def backstage(request):
    today=datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    todayDone=User_Done.objects.filter(time__lt=tomorrow,time__gte=today)
    AllDone=User_Done.objects.all()
    winCan=Winner_Done.objects.filter(prize='CAN320ml焦糖韋恩咖啡乙箱')
    winCanToday=Winner_Done.objects.filter(prize='CAN320ml焦糖韋恩咖啡乙箱',time__lt=tomorrow,time__gte=today)
    winFin=Winner_Done.objects.filter(prize='FIN旅行洗漱包乙個')
    winFinToday=Winner_Done.objects.filter(prize='FIN旅行洗漱包乙個',time__lt=tomorrow,time__gte=today)
    prizeObject=Prize_Rate.objects.filter(today=today)
    prize_rate={}
    prize_left={}
    for i in prizeObject:
        prize_rate[i.index]=i.rate
        prize_left[i.index]=i.left
    prize_rate2=json.dumps(prize_rate)
    prize_left2=json.dumps(prize_left)
    a=request.GET.get('a','')
    p=request.GET.get('p','')
    if(a=='admin' and p=='admin'):
        return render(request,'backstage.html',locals())
    else:
        return render(request,'error.html',locals())
def backstageEdit(request):
    index=request.POST['index']
    rate=request.POST['rate']
    left=request.POST['left']
    today=datetime.date.today()
    Prize_Rate.objects.filter(index=index,today=today).update(rate=rate)
    Prize_Rate.objects.filter(index=index,today=today).update(left=left)
    return HttpResponse("表單回傳成功") 
def winner(request):
    allWinner=Winner_Done.objects.all()
    post_list = serializers.serialize('json', allWinner)
    a=request.GET.get('a','')
    p=request.GET.get('p','')
    if(a=='admin' and p=='admin'):
        return HttpResponse(post_list, content_type="text/json-comment-filtered;charset=utf-8")
    else:
        return render(request,'error.html',locals())
def player(request):
    allPlayer=User_Done.objects.all()
    post_list = serializers.serialize('json', allPlayer)
    a=request.GET.get('a','')
    p=request.GET.get('p','')
    if(a=='admin' and p=='admin'):
        return HttpResponse(post_list, content_type="text/json-comment-filtered;charset=utf-8")
    else:
        return render(request,'error.html',locals())
