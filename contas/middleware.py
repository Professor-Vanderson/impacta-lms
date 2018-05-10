from django.shortcuts import redirect
from contas.models import Sessao

class SessaoCustomizadaMiddleware(object):
    _sessionId = "SESSAOID"
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path_info.startswith("/static/"):
            if self._sessionId in request.COOKIES:
                cookie = request.COOKIES[self._sessionId]
                if cookie != "None":
                    sessao = Sessao.objects.get(id=cookie)
                    request.sessao = sessao
            
        response = self.get_response(request)
    
        if hasattr(request, "sessao"):
            response.set_cookie(self._sessionId, request.sessao.id)
        else:
            response.delete_cookie(self._sessionId)

        return response

class AutorizacaoMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info
        if path.startswith("/contas/") and not hasattr(request, "sessao"):
            return redirect("/entrar/")
        else:
            return self.get_response(request)
