from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def submissions(request):
    return render(request, 'submissions.html')

def submission(request):
    return HttpResponse('Individual Submission')