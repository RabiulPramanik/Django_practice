from django.urls import path
from . import views

urlpatterns = [
    path('singup/', views.singupview.as_view(), name="singuppage"),
    path('login/', views.loginview.as_view(), name="loginpage"),
    path('logout/', views.logoutView.as_view(), name='logout')
    
]