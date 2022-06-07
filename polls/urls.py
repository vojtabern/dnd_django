from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('character/<int:pk>', views.CharacterDetailView, name='character_detail'),
    path('class/<str:pk>', views.ClassDetailView, name='class_detail'),
    path('playerlist/', views.PlayerListView.as_view(), name='player_list'),
]
