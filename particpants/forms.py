# from django import forms
from django.core import validators
from django.core.validators import RegexValidator
from django import forms
from .models import Participant, Categorie


class InscriptionParticipantForm(forms.ModelForm):
    class Meta:
        prenom_participant = forms.CharField()
        model = Participant
        fields = [
            'prenom_participant',
            'nom_participant',
            'courriel_participant',
            'date_naissance',
            'categories'
        ]
        labels = {
            'prenom_participant': 'Votre prénom',
            'nom_participant': 'Votre nom',
            'courriel_participant': 'Votre courriel',
            'date_naissance': 'Votre date de naissance',
            'categories': 'Le ou les catégories dans lesquelles vous vous inscrivez'
        }
        error_messages = {
            'prenom_participant': {
                'max_length': "Votre prénom dépasse le nombre de caractères permis.",
            },
        }

    def clean_prenom_participant(self):
        regex_noms = RegexValidator('^[A-zÀ-ÿ -\']$', "Votre prénom ne doit contenir que des lettres, des traits d'union, des apostrophes ou des espaces.")
        prenom_participant = self.cleaned_data.get("prenom_participant")
        regex_noms('prenom_participant')


# class InscriptionForm(ModelForm):
#     class Meta:
#         model = Categorie.participants.through
#         fields = [
#             'nom_categorie',
#             'participants'
#         ]
#         widgets = {}


# class RegexValidator:
#     regex = '',
#     message = '',
#     code = '',
#     inverse_match = False,
#     flags = 0,
#
#     def __init__(self, regex=None, message=None, code=None, inverse_match=None, flags=None):
#         if regex is not None:
#             self.regex = regex
#         if message is not None:
#             self.message = message
#         if code is not None:
#             self.code = code
#         if inverse_match is not None:
#             self.inverse_match = inverse_match
#         if flags is not None:
#             self.flags = flags
#
#     def __call__(self, value):

