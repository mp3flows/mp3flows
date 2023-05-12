from django.contrib import admin
from .models import Music, Ads, FreeBeat

# listing models 

class ListMusic(admin.ModelAdmin):
 list_display = ('musicname',)

class ListAds(admin.ModelAdmin):
 list_display = ('adsname',)

class ListFreeBeat(admin.ModelAdmin):
 list_display = ('beatname',)

# Register your models here.
admin.site.register(Music, ListMusic)
admin.site.register(Ads, ListAds)
admin.site.register(FreeBeat,ListFreeBeat)
