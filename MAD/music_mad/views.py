from django.shortcuts import render
from .models import Music, Ads, FreeBeat
from django.db.models import Q
# Create your views here.
def index(request):
    true_ads = True

    try:
        true_ads = True
        ads = Ads.objects.get(id=2)

        q = request.GET.get('q')
        print(request.GET)
        if q != None:
            getmusic = Music.objects.filter(
                Q(musicname__icontains=q)|
                Q(artistname__icontains=q)).order_by('-created')
        else:
            ads = Ads.objects.get(id=2)
            q = ''
            getmusic = Music.objects.all().order_by('-created')[:7]
    except Exception:
        true_ads = False
        getmusic = Music.objects.all().order_by('-created')[:7]

        return render(request, 'music_mad/music.html', {
        'musicsfilt':getmusic,
        'ads':None,
        'true_ads':true_ads


    })

    return render(request, 'music_mad/music.html', {
        'musicsfilt':getmusic,
        'ads':ads,
        'true_ads':true_ads
    })


def download(request, id):
    true_ads = True

    try:
        true_ads = True
        
        ads = Ads.objects.get(id=2)

        idget = Music.objects.get(id=id)
    except Exception:
        true_ads = False
        idget = Music.objects.get(id=id)
        

        return render(request, 'music_mad/base.html', {
        'musics':idget,
        'ads':None,
        'true_ads':true_ads


    })

    return render(request, 'music_mad/base.html', {
        'musics':idget,
        'ads':ads,
        'true_ads':true_ads

        })


def free_beat(request):
    true_ads = True

    try:
        true_ads = True

        ads = Ads.objects.get(id=2)
        q = request.GET.get('q')
        print(request.GET)
        if q != None:
            getmusic = FreeBeat.objects.filter(
                Q(beatname__icontains=q)).order_by('created')
        else:
            ads = Ads.objects.get(id=2)
            q = ''
            getmusic = FreeBeat.objects.filter(
                Q(beatname__icontains=q)).order_by('created') 
    except Exception:
        true_ads = False
        getmusic = FreeBeat.objects.all()
        return render(request, 'music_mad/free_beat.html', {
        'musicsfilt':getmusic,
        'ads':None,
        'true_ads':true_ads


    })
            
    return render(request, 'music_mad/free_beat.html', {
        'musicsfilt':getmusic,
        'ads':ads,
        'true_ads':true_ads


    })

def free_beat_download(request, id):
    true_ads = True

    try:
        true_ads = True

        ads = Ads.objects.get(id=2)

        idget = FreeBeat.objects.get(id=id)
    except Exception:
        true_ads = False
        idget = FreeBeat.objects.get(id=id)

        return render(request, 'music_mad/free_download.html', {
        'musics':idget,
        'ads':None,
        'true_ads':true_ads


    })    
    return render(request, 'music_mad/free_download.html', {
        'musics':idget,
        'ads':ads,
        'true_ads':true_ads

        })

def see_all(request):
    true_ads = True

    try:
        true_ads = True


        ads = Ads.objects.get(id=2)

        seeallmusic = Music.objects.all().order_by('-created')
    except Exception:
        true_ads = False
        seeallmusic = Music.objects.all().order_by('-created')
        
        return render(request, 'music_mad/see_all.html', {
        'musics':seeallmusic,

        'ads':None,
        'true_ads':true_ads


    })   
    return render(request, 'music_mad/see_all.html', {
        'musics':seeallmusic,
        'ads':ads,
        'true_ads':true_ads

        })

