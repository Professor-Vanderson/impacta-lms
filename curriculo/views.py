from django.shortcuts import render

def lista(request, curso = ""):
    if curso.upper() == "ADS":
        return render(request, "ADS.html")
    else:
        return render(request, "lista.html")