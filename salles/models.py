from django.db import models

class Salle(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    capacite = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    disponible = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    def __Meta__(self):
        verbose_name = "Salle"
        verbose_name_plural = "Salles"
