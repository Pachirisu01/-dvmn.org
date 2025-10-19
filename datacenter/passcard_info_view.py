from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import datetime
from django.shortcuts import get_object_or_404


def is_visit_long(visit, minutes=60):
    if not visit.leaved_at:
        return False
    duration = visit.leaved_at - visit.entered_at
    return duration > datetime.timedelta(minutes=minutes)


def passcard_info_view(request, passcode):

    passcard =  get_object_or_404(Passcard,passcode=passcode)

    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        if visit.leaved_at:
            duration = visit.leaved_at - visit.entered_at
        else:
            duration = timezone.now() - visit.entered_at    

        visit_info = {
        'entered_at': timezone.localtime(visit.entered_at),
        'duration': duration,
        'is_strange': is_visit_long(visit),
        }

        this_passcard_visits.append(visit_info)

    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


