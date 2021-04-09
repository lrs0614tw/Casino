from django.contrib import admin

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
class spinwheel_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','time')
admin.site.register(spinwheel_Done,spinwheel_Done_Admin)
class hui_Done_Admin(admin.ModelAdmin):
    list_display = ('uid','prize','time')
admin.site.register(hui_Done,hui_Done_Admin)
# Register your models here.
