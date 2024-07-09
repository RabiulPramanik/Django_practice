from django.urls import path
from . import views


urlpatterns = [
    path('', views.album, name="albumpage"),
    path('edit/<int:id>', views.edit_album, name="edit"),
]