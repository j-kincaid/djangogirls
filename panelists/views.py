from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def panelists(request):
    return HttpResponse('Our panelists')

def panelist(request, pk):
    return HttpResponse('Panelist:' + ' ' + str(pk))