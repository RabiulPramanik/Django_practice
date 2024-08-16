from django.shortcuts import render, redirect
from .form import UserCreateForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def singup_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreateForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Created Successfully")
                return redirect("singuppage")
        else:
            form = UserCreateForm()
        return render(request, "createForm.html", {'form':form, 'type':'SingUp'})
    else:
        return redirect("profilepage")

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username=username, password = user_pass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully")
                    return redirect("profilepage")
        else:
            form = AuthenticationForm()
        return render(request, "createForm.html", {'form':form, 'type':'Login'})
    else:
        return redirect("profilepage")

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("homepage")

@login_required
def password_change_with_old(request):
    if request.method == 'POST':
        change_form = PasswordChangeForm(request.user, data = request.POST)
        if change_form.is_valid():
            change_form.save()
            messages.success(request, "Change password successfully!")
            return redirect("profilepage")
    else:
        change_form = PasswordChangeForm(user = request.user)
    return render(request, "changeForm.html", {'form':change_form, 'type':'Password Change with old Password'})

@login_required
def password_change_without_old(request):
    return render(request, "changeForm.html")

@login_required
def profile(request):
    return render(request, "profile.html")




