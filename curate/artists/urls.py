from django.urls import path
from . import views

urlpatterns = [
    path('artists/<str:pk>/', views.artists, name='artists'),
    path('artist/<str:pk>/', views.artist, name='artist'),
]