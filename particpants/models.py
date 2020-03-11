from django.db import models


class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=200)
    description_categorie = models.CharField(max_length=600)

    def __str__(self):
        return self.nom_categorie


# *** relation Many to many défini seulement dans la classe Participant,
# puisque rien ne sera ajouté à la table d'intersection
class Participant(models.Model):
    nom_participant = models.CharField(max_length=200)
    prenom_participant = models.CharField(max_length=200)
    courriel_participant = models.EmailField(max_length=300)
    date_naissance = models.DateField()
    actif = models.BooleanField('est présentement actif')
    categories = models.ManyToManyField(Categorie)

    def __str__(self):
        return self.prenom_participant + " " + self.nom_participant

    def nom_complet(self):
        return self.prenom_participant + " " + self.nom_participant



