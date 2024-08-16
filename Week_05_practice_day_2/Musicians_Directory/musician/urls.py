from django.urls import path
from . import views

urlpatterns = [
    path('musician_add/', views.createview.as_view(), name="musician_addpage"),
    path('musician_add/eidt<int:id>/', views.editMusician.as_view(), name="editmusicianpage"),
]