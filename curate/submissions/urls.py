from django.urls import path
from . import views

urlpatterns = [
    path('submissions/', views.submissions, name='submissions'),
    path('submission/<str:pk>/', views.submission, name='submission'),
]