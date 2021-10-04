from django.shortcuts import render
from django.http import HttpResponse


def panelists(request):
    return render(request, 'panelists.html')

def panelist(request, pk):
    return HttpResponse('Panelist:' + ' ' + str(pk))