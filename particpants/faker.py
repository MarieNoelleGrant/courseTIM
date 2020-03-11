from faker import Faker

from .models import Participant, Categorie

objFaker = Faker()


def seed(n=10):

    num = 1
    for i in range(n):
        prenom = objFaker.first_name()
        nom = objFaker.last_name()
        courriel = objFaker.email()
        naissance = objFaker.date_between(start_date='-70y', end_date='-18y')
        etat_actif = objFaker.pybool()

        Participant.objects.get_or_create(prenom_participant=prenom, nom_participant=nom, courriel_participant=courriel, date_naissance=naissance, actif=etat_actif)

        num += 1


if __name__ == '__main__':
    print("En processus de faker")
    seed(10)
    print("Faking terminé!")
