from django.shortcuts import render
from django.http import HttpResponse


def golowna(request):
    return render(request, 'main/golowna.html')


def about(request):
    return render(request, 'main/about.html')


def prikol(request):
    return render(request, 'main/prikol.html')


def iz(request):
    return render(request, 'main/iz.html')


def изменения(request):
    return render(request, 'main/изменения.html')