from django.urls import path, include

from .views import index, entrar, sair

urlpatterns = [
    path('', index),
    path("entrar/", entrar, name="entrar"),
    path("sair/", sair, name="sair")
]