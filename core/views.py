from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from contas.backend import autenticar
from contas.models import Sessao

def index(request):
    return render(request, "index.html")

def ads(request):
    return render(request, "ads.html")

def entrar(request):
    context = {}
    if request.POST:
        if autenticar(request):
            return redirect("/")
        else:
            context["erro"] = "Usuário ou senha não estão corretos"
    return render(request, "login.html", context)

def sair(request):
    if request.sessao:
        request.sessao.delete()
    return redirect("/")