from django.urls import path
from . import views

urlpatterns = [
    path('album_add/', views.AlbumCreate.as_view(), name="album_addpage"),  
    path('album_add/edit<int:id>/', views.editview.as_view(), name="editpage"),
    path('album_add/delete<int:id>/', views.deleteview.as_view(), name="deletepage"),
]