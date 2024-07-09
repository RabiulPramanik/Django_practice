from django.urls import path
from . import views


urlpatterns = [
    path('', views.musician, name="musicianpage"),
    path('delete/<str:email>', views.delete_musician, name="delete_musician"),
    path('edit/<str:email>', views.edit_musician, name="edit_musician"),
]