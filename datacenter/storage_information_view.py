from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.getting_duration import get_formatted_duration


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    
    non_closed_visits = []

    for visit in active_visits:
        formatted_duration = get_formatted_duration(visit)
        
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': formatted_duration,
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
