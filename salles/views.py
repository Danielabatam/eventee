from django.shortcuts import render
from .models import Salle

def liste_salles(request):
    salles = Salle.objects.all()
    return render(request, 'salles/liste_salles.html', {'salles': salles})
