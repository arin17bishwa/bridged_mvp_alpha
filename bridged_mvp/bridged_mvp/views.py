from django.shortcuts import HttpResponse, render


def loader_io(request):
    return HttpResponse('loaderio-39cf266dd5a723050b3f3fa395391151')


def home(request):
    return render(request, 'bridged_mvp/home.html')
