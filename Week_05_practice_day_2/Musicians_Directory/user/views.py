from django.shortcuts import render, redirect
from .form import CreateUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View

class singupview(FormView):
    template_name = "form.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("homepage")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("homepage")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Account Created Successfully")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Singup'
        return context
    
class loginview(LoginView):
    template_name = 'form.html'
    
    def form_valid(self, form):
        messages.success(self.request, "Logged Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, "Not valid information!")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["typy"] = 'Login'
        return context
    
    def get_success_url(self):
        return reverse_lazy("homepage")
    
class logoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("loginpage")
    
    


