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
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from turntableApp import views
from django.conf import settings
from django.conf.urls. static import static
from rest_framework.authtoken import views as tokenViews

router = DefaultRouter()
router.register('heysongUid', views.heysongUidViewSet)

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
    path('snakeUpdate',views.snakeUpdate),
    path('scratchDone', views.scratchDone),
    url('^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('heysongScratch', views.heysongScratch),
    path('api-token-auth/', tokenViews.obtain_auth_token),
    path('heysongScratchForm',views.heysongScratchForm),
    path('heysongScratch_form_done', views.heysongScratchFormDone),
    path('heysongScratch_all_done', views.heysongScratchAllDone),
    path('liffHeysongScratch', views.liffHeysongScratch),
    path('HeysongScratchplayer',views.HeysongScratchplayer),
    path('heysongScratchbackstage',views.heysongScratchbackstage),
    path('heysongScratchRecord',views.heysongScratchRecord),
    path('gameTraveltobuys',views.gameTraveltobuys),
    path('liffTraveltobuys',views.liffTraveltobuys),
    path('gameFormTraveltobuys',views.gameFormTraveltobuys),
    path('form_doneTraveltobuys', views.formDoneTraveltobuys),
    path('all_doneTraveltobuys', views.allDoneTraveltobuys),
    path('liffScratchJie', views.liffScratchJie),
    path('jieScratch', views.jieScratch),
    path('jieGameDone', views.jieGameDone),
    path('xiaodu', views.xiaodu),
    path('liffTravelMember',views.liffTravelMember),
    path('liffScratchPei', views.liffScratchPei),
    path('peiScratch', views.peiScratch),
    path('peiGameDone', views.peiGameDone),
    path('zhongyuan', views.zhongyuan),
    path('puduliff', views.puduliff),
    path('zhongyuantest', views.zhongyuantest),
    path('createpudushare', views.createpudushare),
    path('fileupload', views.fileupload),
    path('sharefileupload', views.sharefileupload),
    path('zhongyuanMgmliff', views.zhongyuanMgmliff),
    
]
def page_not_found(request, exception):
    return render(request, 'error.html')
handler404 = page_not_found
urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)