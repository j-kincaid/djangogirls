from django.urls import path
from . import views

urlpatterns = [
    path('panelists/<str:pk>/', views.panelists, name='panelists'),
    path('panelist/<str:pk>/', views.panelist, name='panelist'),
]