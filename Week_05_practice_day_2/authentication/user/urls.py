from django.urls import path
from .views import home, singup_user, login_user, logout_user, password_change_with_old, password_change_without_old, profile

urlpatterns = [
    path('', home, name="homepage"),
    path('singup/', singup_user, name="singuppage"),
    path('login/', login_user, name="loginpage"),
    path('logout/', logout_user, name="logoutpage"),
    path('profile/', profile, name="profilepage"),
    path('pass_with/', password_change_with_old, name="pass_with_page"),
    path('pass_without/', password_change_without_old, name="pass_without_page"),
]