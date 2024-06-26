from django.shortcuts import render
from Musician.models import Musician
from Album.models import Album
def home(request):
    music = Musician.objects.all()
    album = Album.objects.all()
    return render(request, 'home.html',{'data': music, 'ans':album})

