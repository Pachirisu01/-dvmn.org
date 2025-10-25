from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datetime
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datacenter.getting_duration import is_visit_long, get_duration, format_duration, get_formatted_duration


def passcard_info_view(request, passcode):

    passcard =  get_object_or_404(Passcard,passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        formatted_duration = get_formatted_duration(visit)

        visit_info = {
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': formatted_duration,
            'is_strange': is_visit_long(visit),
        }


        this_passcard_visits.append(visit_info)

    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


