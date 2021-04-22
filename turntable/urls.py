"""turntable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from turntableApp import views
from django.conf import settings
from django.conf.urls. static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('liff',views.liff),
    path('game',views.game),
    path('gameForm',views.gameForm),
    path('game_done', views.gameDone),
    path('form_done', views.formDone),
    path('all_done', views.allDone),
    path('8HNSQPhDGFHkXezG', views.backstage),
    path('backstageEdit', views.backstageEdit),
    path('winner',views.winner),
    path('player',views.player),
    path('gameDemo',views.gameDemo),
    path('gameDemo_done', views.gameDemoDone),
    path('liffDemo', views.liffDemo),
    path('achi', views.achi),
    path('liffAchi', views.liffAchi),
    path('liffClaire', views.liffClaire),
    path('claire_done', views.claireDone),
    path('liffScratch', views.liffScratch),
    path('scratchOff', views.scratchOff),
    path('liffScratchHui', views.liffScratchHui),
    path('huiScratch', views.huiScratch),
    path('huiGameDone', views.huiGameDone),
    path('slotDemo',views.slotDemo),
    path('liffSlot',views.liffSlot),
    path('slotUpdate',views.slotUpdate),
    path('liffScratchWen', views.liffScratchWen),
    path('wenScratch', views.wenScratch),
    path('wenGameDone', views.wenGameDone),
    path('liffSnake', views.liffSnake),
    path('snake',views.snake),
    path('snakeUpdate',views.snakeUpdate)
    
]
def page_not_found(request, exception):
    return render(request, 'error.html')
handler404 = page_not_found
