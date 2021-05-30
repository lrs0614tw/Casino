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
from turntableApp.serializers import heysongUidSerializer
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

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
class heysongUidViewSet(viewsets.ModelViewSet):
    queryset = heysongUid.objects.all()
    serializer_class = heysongUidSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
class heysongScratch(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'heysongScratch.html'
    def get(self,request):
        uid = request.GET.get('uid','')
        iv = b"VFNSJQXI0P6IZ7UC"
        key = b"HQR9NSTXMCY7R463"
        cipher = AES.new(key, AES.MODE_CBC, iv)
        enc = base64.b64decode(uid)
        deco_uid = unpad(cipher.decrypt(enc), AES.block_size).decode()
        uid=deco_uid
        today=datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        ifCanPlay=1
        prize_object=HeysongScratch_Prize_Rate.objects.all()
        prize_rate={}
        prize_left={}
        prize_prize={}
        for i in prize_object:
            prize_rate[i.index]=int(i.rate)
            prize_left[i.index]=int(i.left)
            prize_prize[i.index]=i.prize
        j = {}
        sum = 0
        for i in range(4):
            if (prize_left[str(i)] > 0 and prize_rate[str(i)]> 0):
                sum = sum + prize_rate[str(i)]
        jsonCount = 0
        for i in range(4):
            if (prize_left[str(i)] > 0 and prize_rate[str(i)]> 0):
                j[str(i)] = (prize_rate[str(i)] / sum) + jsonCount
                jsonCount = jsonCount + (prize_rate[str(i)] / sum)
            else:
                j[str(i)] = -1
            index = -1
            rand = random.random()
        for i in [3,2,1,0]:
            if (prize_left[str(i)] > 0):
                if (j[str(i)] > rand):
                    index = i
        if(HeysongScratch_Winner_Done.objects.filter(uid=uid).exists()):
            index=3
        if (index < 0):
            index = 3
        print(index)
        newleft=prize_left[str(index)]-1
        print(index,newleft)
        HeysongScratch_Prize_Rate.objects.filter(index=index).update(left=newleft)
        if(HeysongScratch_User_Done.objects.filter(uid=uid,time__lt=tomorrow,time__gte=today).exists()==True):
            if(HeysongScratch_Winner_Done.objects.filter(uid=uid,time__lt=tomorrow,time__gte=today).exists()):
                index=3
                ifCanPlay=0
            else:
                user=HeysongScratch_User_Done.objects.filter(uid=uid,time__lt=tomorrow,time__gte=today)
                prize=user[0].name
                if(prize!='明日再試！'):
                    if(prize=='PKL250FIN乳酸菌補給飲料'):
                        index=0
                    elif(prize=='羅技 Stream Cam 直播攝影機'):
                        index=1
                    elif(prize=='美國BLUE YETI X 專業USB麥克風'):
                        index=2
                    ifCanPlay=0
                else:
                    prize=user[0].name=0
                    index=3   
                    ifCanPlay=0
        elif(uid!=''):
            HeysongScratch_User_Done.objects.create(uid=uid,name=prize_prize[str(index)])
        else:
            ifCanPlay=0
            index=3
        return Response({'uid':uid,'index':index,'ifCanPlay':ifCanPlay})
def heysongScratchForm(request):
    prize=request.GET.get('prize','')
    uid=request.GET.get('uid','')
    return render(request,'heysongScratchForm.html',locals())
@csrf_exempt
def heysongScratchFormDone(request):
    name=request.POST['name']
    phone=request.POST['phone']
    address=request.POST['address']
    district=request.POST['district']
    county=request.POST['county']
    zipcode=request.POST['zipcode']
    prize=request.POST['prize']
    uid=request.POST['uid']
    return render(request,'heysongScratchformDone.html',locals())
@csrf_exempt
def heysongScratchAllDone(request):
    uid=request.POST['uid']
    prize=request.POST['prize']
    name=request.POST['name']
    phone=request.POST['phone']
    address=request.POST['address']
    HeysongScratch_Winner_Done.objects.create(uid=uid,prize=prize,name=name,phone=phone,address=address)
    return HttpResponse("表單回傳成功") 