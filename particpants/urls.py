from django.urls import path

from . import views

# ne pas oublier le namespace
app_name = 'particpants'
urlpatterns = [
    path('', views.index, name='index'),
    path('listeparticipant', views.liste_participants, name='liste_participants'),
    path('listeparticipant/<int:participant_id>', views.detail_participant, name='detail_participant'),
    path('listecategories', views.liste_categories, name='liste_categories'),
    path('inscription', views.inscription, name='inscription')
]
