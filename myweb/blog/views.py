from django.shortcuts import render
def index(request):
    return render(request, 'blog/index.html')

def contacto(request):
    return render(request, 'blog/contacto.html')

def servicio(request):
    return render(request, 'blog/servicio.html')


