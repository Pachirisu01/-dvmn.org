from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    # Программируем здесь
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    
    non_closed_visits = []

    for visit in active_visits:
        duration = timezone.now() - visit.entered_at
        hours = int(duration.total_seconds() // 3600)
        minutes = int((duration.total_seconds() % 3600) // 60)

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': f'{hours}ч {minutes}мин',
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
