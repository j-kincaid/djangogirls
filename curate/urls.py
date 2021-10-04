from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def panelists(request):
    return HttpResponse('Our panelists')
def panelist(request, pk):
    return HttpResponse('Panelist:' + ' ' + str(pk))


def artists(request):
    return HttpResponse('Submitting Artists')
def artist(request,pk):
    return HttpResponse('Individual Artist')


def submissions(request):
    return HttpResponse('Submissions')
def submission(request,pk):
    return HttpResponse('Individual Submission')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('artists.urls')),
    path('', include('panelists.urls')),
    path('', include('submissions.urls')),
]
