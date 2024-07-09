from django.shortcuts import render
from .form import DjangoForm

def home(request):
    if request.method == 'POST':
        newform = DjangoForm(request.POST)
        if newform.is_valid():
            print(newform.cleaned_data)
    else:
        newform = DjangoForm()
    return render(request, "home.html", {'form': newform})
