from django.db import models

class Employee(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):

        return self.nom