from django.shortcuts import render, redirect
from .form import AlbumForm
from .models import AlbumModel

def album(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect("albumpage")

    else:
        album_form = AlbumForm()
    return render(request, "album.html", {'form':album_form})

def edit_album(request, id):
    ad = AlbumModel.objects.get(pk=id)
    album_form = AlbumForm(instance=ad)

    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=ad)
        if album_form.is_valid():
            album_form.save()
            return redirect("homepage")
        
    return render(request, "album.html", {'form':album_form})
