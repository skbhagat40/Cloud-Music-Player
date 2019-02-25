from django.shortcuts import render
from django.http import HttpResponse
from .models import Album,Song
from django.shortcuts import render,get_object_or_404
from django.http import Http404
# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    
    return render(request,'music/index.html',context)

def detail(request,album_id):
    try:
        album = Album.objects.get(id = album_id)
    except Album.DoesNotExist:
        raise Http404("SOrry! the album does not exist!")
    context = {'album' : album}
    html1 = "<h1>The album id is" + str(album_id) + "</h1>"
    html1 += "<h1><br>The artist is:" + Album.objects.get(id = album_id).artist+ "</h1>"
    return render(request,'music/detail.html',context)

def favorite(request,album_id):
    album = get_object_or_404(Album,id = album_id)
    try:
        selected_song = album.song_set.get(id = request.POST['song'])
    except:
        return render(request,'music/detail.html',{'album':album,'error_message':'No song selected!!'})
    else:
        selected_song.isFavorite = True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})

def unfavorite(request,album_id):
    album = get_object_or_404(Album,id = album_id)
    try:
        selected_song = album.song_set.get(id = request.POST['song'])
    except:
        return render(request,'music/detail.html',{'album':album,'error_message':'No song selected!!'})
    else:
        selected_song.isFavorite = False
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})
