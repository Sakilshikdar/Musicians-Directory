
from django.urls import path
from .import views

urlpatterns = [
    path('', views.MusicianListView.as_view(), name='musician'),
    path('create/', views.MusicianCreateView.as_view(), name='musician_list'),
    path('musician/<int:pk>/edit/', views.
         MusicianUpdateView.as_view(), name='musician_edit'),
    path('musician/<int:pk>/delete/', views.
         MusicianDeleteView.as_view(), name='musician_delete'),
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('album/add/', views.AlbumCreateView.as_view(), name='album_add'),
    path('album/<int:pk>/edit/', views.AlbumUpdateView.as_view(), name='album_edit'),
    path('album/<int:pk>/delete/',
         views.AlbumDeleteView.as_view(), name='album_delete'),
]
