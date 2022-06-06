from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('character/<int:pk>', views.CharacterDetailView, name='character_detail'),
    path('class/<str:pk>', views.ClassDetailView.as_view(), name='class_detail'),
]
