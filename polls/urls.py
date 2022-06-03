from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('class/<int:pk>', views.ClassDetailView.as_view(), name='class_detail'),
]
