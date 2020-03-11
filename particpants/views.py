from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import Participant, Categorie
from .forms import InscriptionParticipantForm


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
        'participant': participant
    }
    return render(request, 'particpants/detailparticipant.html', context)


def liste_categories(request):
    toutes_categories = Categorie.objects.order_by('nom_categorie')
    context = {
        'toutes_categories': toutes_categories,
        'participants': Participant.objects.all
    }
    return render(request, 'particpants/listecategories.html', context)


def inscription(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InscriptionParticipantForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = InscriptionParticipantForm

    context = {
        'form': form
    }
    return render(request, 'particpants/inscription.html', context)
