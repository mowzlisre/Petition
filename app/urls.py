from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.newPetition, name="new-petition"),
]
