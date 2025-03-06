from django.shortcuts import render


def myapp(request):
    return render(request, 'main.html', {})


def login(request):
    return render(request, 'main.html', {})
