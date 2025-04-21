from django.urls import path

from controle_interno import views

urlpatterns = [
    path('', views.index, name='index'),
]
