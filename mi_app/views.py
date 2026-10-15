from django.shortcuts import render


def historia_view(request):
    return render(request, 'historia.html')


def visual_view(request):
    return render(request, 'visual.html')