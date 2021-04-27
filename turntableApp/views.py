from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
import datetime
import json
import random
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
def gameDemo(request):
    uid = request.GET.get('uid','')
    return render(request,'gameDemo.html',locals())
def gameDemoDone(request):
    uid=request.POST['uid']
    Userdemo_Done.objects.create(uid=uid)
    return HttpResponse("表單回傳成功") 
def liffDemo(request):
    finish=request.GET.get('finish','')
    return render(request,'liffDemo.html',locals())
def liffAchi(request):
    return render(request,'liffAchi.html',locals())
def achi(request):
    uid = request.GET.get('uid','')
    displayname = request.GET.get('displayname','')
    pictureurl = request.GET.get('pictureurl','')
    if(Userdemo_Done.objects.filter(uid=uid).exists()):
        print('a')
        gameDone=1
    if(claire_Done.objects.filter(uid=uid).exists()):
        claireDone=1
    if(scratchDemo_Done.objects.filter(uid=uid).exists()):
        scratchDone=1
    return render(request,'Achi.html',locals())
def liffClaire(request):
    return render(request,'liffClaire.html',locals())
def claireDone(request):
    uid=request.POST['uid']
    today=datetime.date.today()
    claire_Done.objects.create(uid=uid,time=today)
    return HttpResponse("表單回傳成功") 
def liffScratch(request):
    return render(request,'liffScratch.html',locals())
def scratchOff(request):
    uid = request.GET.get('uid','')
    displayname = request.GET.get('displayname','')
    pictureurl = request.GET.get('pictureurl','')
    index=random.randint(0,2)
    print(index)
    return render(request,'scratchOff.html',locals())
def liffScratchHui(request):
    finish=request.GET.get('finish','')
    return render(request,'liffScratchHui.html',locals())
def huiScratch(request):
    uid = request.GET.get('uid','')
    if(hui_Done.objects.filter(uid=uid).exists()==True):
        info=hui_Done.objects.filter(uid=uid)
        finish='1'
        print(finish)
        prize=info[0].prize
        if(prize=='台灣好浴皂'):
            index=0
        else:
            index=1
    else:
        finish='0'
        r=random.randint(0,9)
        if(r>=3):
            index=1
        else:
            index=0
    return render(request,'huiScratch.html',locals())
def huiGameDone(request):
    uid=request.POST['uid']
    prize=request.POST['prize']
    today=datetime.date.today()
    hui_Done.objects.create(uid=uid,prize=prize)
    return HttpResponse("表單回傳成功") 
def slotDemo(request):
    uid = request.GET.get('uid','')
    if(slot_info.objects.filter(uid=uid).exists()):
        score=slot_info.objects.filter(uid=uid)[0].score
    else:
        slot_info.objects.create(uid=uid,score=50,invite=0)
        score=50
    return render(request,'slotDemo.html',locals())
def liffSlot(request):
    return render(request,'liffSlot.html',locals())
def slotUpdate(request):
    uid=request.POST['uid']
    score=request.POST['score']
    slot_info.objects.filter(uid=uid).update(score=score)
    return HttpResponse("表單回傳成功") 
def liffScratchWen(request):
    finish=request.GET.get('finish','')
    return render(request,'liffScratchWen.html',locals())
def wenScratch(request):
    uid = request.GET.get('uid','')
    if(wen_Done.objects.filter(uid=uid).exists()==True):
        info=wen_Done.objects.filter(uid=uid)
        finish='1'
        print(finish)
        prize=info[0].prize
        if(prize=='恭喜獲得乾洗手！'):
            index=0
        else:
            index=1
    else:
        finish='0'
        r=random.randint(0,9)
        if(r>=3):
            index=1
        else:
            index=0
    return render(request,'wenScratch.html',locals())
def wenGameDone(request):
    uid=request.POST['uid']
    prize=request.POST['prize']
    today=datetime.date.today()
    wen_Done.objects.create(uid=uid,prize=prize)
    return HttpResponse("表單回傳成功") 
def liffSnake(request):
    return render(request,'liffSnake.html',locals())
def snake(request):
    uid = request.GET.get('uid','')
    displayname = request.GET.get('displayname','')
    pictureurl = request.GET.get('pictureurl','')
    if(snake_Player.objects.filter(uid=uid).exists()==False):
        snake_Player.objects.create(uid=uid,name=displayname,picture=pictureurl,highscore=0,prize=0)
    highscore=snake_Player.objects.filter(uid=uid)[0].highscore
    winnerList=snake_Player.objects.all().order_by('-highscore')[:5]     
    return render(request,'snake.html',locals())
@csrf_exempt
def snakeUpdate(request):
    uid=request.POST['uid']
    highscore=request.POST['highscore']
    snake_Player.objects.filter(uid=uid).update(highscore=highscore)
    return HttpResponse("表單回傳成功") 
def scratchDone(request):
    uid=request.POST['uid']
    scratchDemo_Done.objects.create(uid=uid)
    return HttpResponse("表單回傳成功") 