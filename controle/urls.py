from django.urls import path

from controle import views

urlpatterns = [
    path('', views.index, name='index'),
]
