from django.utils import timezone
import datetime

def is_visit_long(visit, minutes=60):
	if not visit.leaved_at:
		return False
	duration = visit.leaved_at - visit.entered_at
	return duration > datetime.timedelta(minutes=minutes)


def get_duration(visit):
	if visit.leaved_at:
		return visit.leaved_at - visit.entered_at
	else:
		return timezone.now() - visit.entered_at


def format_duration(duration):
	seconds_in_hour = 3600
	minutes_in_hour = 60
	hours_in_storage = int(duration.total_seconds() // seconds_in_hour)
	minutes_in_storage = int((duration.total_seconds() % seconds_in_hour) // minutes_in_hour)
	return f"{hours_in_storage}ч {minutes_in_storage}мин"

def get_formatted_duration(visit):
	duration = get_duration(visit)
	return format_duration(duration)