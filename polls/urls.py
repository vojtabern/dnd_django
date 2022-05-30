from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('class/detail/', views.ClassDetailView.as_view(), name='class_detail'),
]
