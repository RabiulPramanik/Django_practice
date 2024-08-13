from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import AlbumModel
from .form import AlbumForm
from django.urls import reverse_lazy

class AlbumCreate(CreateView):
    model = AlbumForm
    template_name = 'album.html'
    form_class = AlbumForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Album Created'
        return context
    
    
class editview(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("homepage")

class deleteview(DeleteView):
    model = AlbumModel
    template_name = 'del.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("homepage")

