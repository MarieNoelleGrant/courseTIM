# from django import forms
from django.forms import ModelForm
from .models import Participant, Categorie


class InscriptionParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = [
            'prenom_participant',
            'nom_participant',
            'courriel_participant',
            'date_naissance',
            'categories'
        ]


# class InscriptionForm(ModelForm):
#     class Meta:
#         model = Categorie.participants.through
#         fields = [
#             'nom_categorie',
#             'participants'
#         ]
#         widgets = {}
