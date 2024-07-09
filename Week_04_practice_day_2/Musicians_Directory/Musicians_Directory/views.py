from django.shortcuts import render
from album.models import AlbumModel

def home(request):
    data = AlbumModel.objects.all()
    # album_data = data.musician.all()
    return render(request, "home.html", {'data':data})