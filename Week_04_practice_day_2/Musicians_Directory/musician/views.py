from django.shortcuts import render, redirect
from .form import MusicianForm
from .models import MusicianModel

def musician(request):
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("musicianpage")
    else:
        musician_form = MusicianForm()

    return render(request, "musician.html", {'form':musician_form})

def delete_musician(request, email):
    dd = MusicianModel.objects.all()
    for i in dd:
        if i.email == email:
            i.delete()
            return redirect("homepage")
    return redirect("homepage")

def edit_musician(request, email):
    ed = MusicianModel.objects.all()
    for i in ed:
        if i.email == email:
            musician_form = MusicianForm(instance=i)
            if request.method == 'POST':
                musician_form = MusicianForm(request.POST, instance=i)
                if musician_form.is_valid():
                    musician_form.save()
                    return redirect("homepage")
            return render(request, "musician.html", {'form':musician_form})
    return redirect("homepage")
        
            

