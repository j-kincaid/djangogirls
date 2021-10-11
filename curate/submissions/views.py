from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def submissions(request):
    return HttpResponse('Submissions')

def submission(request):
    return HttpResponse('Individual Submission')