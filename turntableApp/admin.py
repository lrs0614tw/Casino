from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

# Register your models here.
from turntableApp.models import *

class User_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','name','time')
admin.site.register(User_Done,User_Done_Admin)
class Winner_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','prize','name','phone','address','time')
admin.site.register(Winner_Done,Winner_Done_Admin)
class Prize_Rate_Admin(admin.ModelAdmin):
    list_display = ('index','prize','rate','left','today')
admin.site.register(Prize_Rate,Prize_Rate_Admin)
class Userdemo_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','time')
admin.site.register(Userdemo_Done,Userdemo_Done_Admin)
class claire_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','time')
admin.site.register(claire_Done,claire_Done_Admin)
class scratchDemo_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','time')
admin.site.register(scratchDemo_Done,scratchDemo_Done_Admin)
class hui_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','prize','time')
admin.site.register(hui_Done,hui_Done_Admin)
class slot_info_Admin(admin.ModelAdmin):
    list_display = ('uid','score','invite')
admin.site.register(slot_info,slot_info_Admin)
class wen_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','prize','time')
admin.site.register(wen_Done,wen_Done_Admin)
class snake_Player_Admin(admin.ModelAdmin):
    list_display = ('uid','name','picture','highscore','prize','time')
admin.site.register(snake_Player,snake_Player_Admin)
class heysongUid_Admin(admin.ModelAdmin):
    list_display = ('uid','time')
admin.site.register(heysongUid,heysongUid_Admin)
class HeysongScratch_User_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','name','time')
admin.site.register(HeysongScratch_User_Done,HeysongScratch_User_Done_Admin)
class HeysongScratch_Winner_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','prize','name','phone','email','address','time')
admin.site.register(HeysongScratch_Winner_Done,HeysongScratch_Winner_Done_Admin)
class HeysongScratch_Prize_Rate_Admin(admin.ModelAdmin):
    list_display = ('index','prize','rate','left','today')
admin.site.register(HeysongScratch_Prize_Rate,HeysongScratch_Prize_Rate_Admin)
class Traveltobuys_User_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','name','time')
admin.site.register(Traveltobuys_User_Done,Traveltobuys_User_Done_Admin)
class Traveltobuys_Winner_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','prize','name','phone','email','address','time')
admin.site.register(Traveltobuys_Winner_Done,Traveltobuys_Winner_Done_Admin)
class Traveltobuys_Prize_Rate_Admin(admin.ModelAdmin):
    list_display = ('index','prize','rate','left','today')
admin.site.register(Traveltobuys_Prize_Rate,Traveltobuys_Prize_Rate_Admin)
class jie_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','prize','time')
admin.site.register(jie_Done,jie_Done_Admin)
class pei_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','prize','time')
admin.site.register(pei_Done,pei_Done_Admin)
class puduImg_Admin(admin.ModelAdmin):
    list_display = ('uid','name','img')
admin.site.register(puduImg,puduImg_Admin)
class ci_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','prize','time')
admin.site.register(ci_Done,ci_Done_Admin)
class mgmlist0809_Admin(admin.ModelAdmin):
    list_display = ('uid','old','new','time')
admin.site.register(mgmlist0809,mgmlist0809_Admin)

# Register your models here.
