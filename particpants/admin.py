from django.contrib import admin

from .models import Participant, Categorie

# VERSION DE BASE DE L'INTERFACE ADMIN
# --------------------------------------------
# admin.site.register(Categorie)
# admin.site.register(Participant)


# VERSION AMÉLIORÉE ET 'CUSTOM'
# --------------------------------------------
class ParticipantInline(admin.TabularInline):
    model = Participant.categories.through

    fieldsets = [
        ('Nom complet', {'fields': ['prenom_participant', 'nom_participant']}),
        (None, {'fields': ['courriel_participant', 'date_naissance', 'actif']}),
    ]

    # Permet de modifier l'interface de liste des questions (selon ce qu'on veut qui y soit affiché)
    list_display = ('nom_complet', 'actif')

    # Ajoute une fenêtre de filtre par date de publication pour la liste
    list_filter = ['actif']

    # Ajoute un champ de recherche par nom de question (question_text)
    search_fields = ['prenom_participant', 'nom_participant', 'actif']


class IntersectionInline(admin.ModelAdmin):
    inlines = [ParticipantInline]


class CategorieAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline]

    list_display = ('nom_categorie', 'description_categorie')
    extra = 1

    # Ajoute une fenêtre de filtre par date de publication pour la liste
    list_filter = ['description_categorie']

    # Ajoute un champ de recherche par nom de question (question_text)
    search_fields = ['nom_categorie']


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Participant)
