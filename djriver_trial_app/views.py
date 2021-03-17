from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect

from river.models import State
from djriver_trial_app.models import AdmissionYearMaster


def trial(request):
    return HttpResponse("trial funtion working.")

# def approve_data(request,id,next_state_id = None):
#     ticket = get_object_or_404(AdmissionYearMaster,pk = id)
#     next_state = get_object_or_404(State, pk=next_state_id)

#     try:
#         ticket.river.status.approve(as_user=request.user, next_state=next_state)
#         return redirect(reverse('admin:djriver_app_admissionyearmaster_changelist'))
#     except Exception as e:
#         return HttpResponse(e.message)


def approve_data(request, id, next_state_id=None):
    data = get_object_or_404(AdmissionYearMaster, pk=id)
    next_state = get_object_or_404(State, pk=next_state_id)

    try:
        data.river.status.approve(as_user=request.user, next_state=next_state)
        print('return')

        return redirect(reverse('admin:dj_river_app_ticket_changelist'))
    except Exception as e:
        print('exception')
        return HttpResponse(e)
