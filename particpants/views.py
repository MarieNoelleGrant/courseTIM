from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import Participant, Categorie


# Create your views here.
def index(request):

    return render(request, 'particpants/index.html')


def liste_participants(request):
    participants_course = Participant.objects.order_by('nom_participant')
    context = {
        'participants_course': participants_course
    }
    return render(request, 'particpants/listeparticipants.html', context)


def detail_participant(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    context = {
        'participant': participant,
        'categorie': Categorie
    }

    return render(request, 'particpants/detailparticipant.html', context)
