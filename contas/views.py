from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from contas.models import Usuario

def listaUsuarios(request):
    context = {
        "usuarios":Usuario.objects.all()
    }
    return render(request, "contas/listUsuario.html", context)

def novoUsuario(request):
    context = {}
    if request.POST:
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confsenha = request.POST.get("confsenha")
        if senha != confsenha:
            context["erro"] = "As senhas não estão iguais"
        else:
            usuario = Usuario.objects.create(
                email=email,
                senha=make_password(senha)
            )
            return redirect("/contas/")
    return render(request, "contas/formUsuario.html", context)

def alterarUsuario(request,id):
    usuario = Usuario.objects.get(id=id)
    context = {
        "usuario":usuario
    }
    if request.POST:
        senha = request.POST.get("senha")
        confsenha = request.POST.get("confsenha")
        if senha != confsenha:
            context["erro"] = "As senhas não estão iguais"
        else:
            usuario.senha=make_password(senha)
            usuario.save()
            return redirect("/contas/")
    return render(request, "contas/formUsuario.html", context)
