from django.shortcuts import render


def historia_view(request):
    return render(request, 'app1/historia.html')


def pagina_view(request):
    return render(request, 'app1/pagina.html')


def visual_view(request):
    return render(request, 'app1/visual.html')


def contacto_view(request):
    return render(request, 'app1/contacto.html')
