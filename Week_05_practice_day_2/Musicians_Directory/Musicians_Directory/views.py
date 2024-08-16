from django.shortcuts import render, redirect
from album.models import AlbumModel
from django.views.generic import ListView

class homeView(ListView):
    model = AlbumModel
    template_name = "home.html"
    context_object_name = 'data'