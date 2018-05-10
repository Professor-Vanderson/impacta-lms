from bcrypt import hashpw, gensalt, checkpw

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from .models import Usuario, Sessao

def autenticar(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    try:
        usuario = Usuario.objects.get(email=email)
        senha = hashpw(senha.encode("utf-8"), usuario.senha.encode("utf-8")).decode()
        if senha == usuario.senha:
            sessao = Sessao.objects.create(usuario=usuario)
            request.sessao = sessao
            return True
        else:
            return False
    except ObjectDoesNotExist:
        return False

