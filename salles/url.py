from django.urls import path
from . import views

urlpatterns = [
    path('salles/', views.liste_salles, name='liste_salles'),
]
