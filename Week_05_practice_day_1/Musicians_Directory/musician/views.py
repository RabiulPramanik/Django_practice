from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import MusicianModel
from .form import MusicianForm
from django.urls import reverse_lazy

class createview(CreateView):
    model = MusicianModel
    template_name = 'create_form.html'
    form_class = MusicianForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        # form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Create Musician'
        return context
    
class editMusician(UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'create_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("homepage")
    
    
