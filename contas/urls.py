from django.urls import path, include

from .views import listaUsuarios, novoUsuario, alterarUsuario

urlpatterns = [
    path('', listaUsuarios),
    path("novo/", novoUsuario),
    path("alterar/<int:id>", alterarUsuario)
]