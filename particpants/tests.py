from django.test import TestCase

# Create your tests here.

from particpants.models import Participant, Categorie
from faker import Faker

objfaker = Faker()


class TestFaker(TestCase):

    def seed(self, n=10):

        num = 1
        for i in range(n):
            prenom = objfaker.first_name()
            nom = objfaker.last_name()
            courriel = objfaker.email()
            naissance = objfaker.date_between(start_date='-70y', end_date='-18y')
            etat_actif = objfaker.pybool()

            Participant.objects.get_or_create(prenom_participant=prenom, nom_participant=nom, courriel_participant=courriel, date_naissance=naissance, actif=etat_actif)

            num += 1

    if __name__ == '__main__':
        print("En processus de faker")
        seed(10)
        print("Faking terminé!")
