from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def artists(request):
    return render(request, 'artists.html')

def artist(request):
    return HttpResponse('Individual Artist')