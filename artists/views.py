from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def artists(request):
    return HttpResponse('Submitting Artists')

def artist(request):
    return HttpResponse('Individual Artist')