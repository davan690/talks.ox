from datetime import date

from django.http.response import Http404
from django.shortcuts import render
from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


def homepage(request):
    return _events_list(request, [])


def upcoming_events(request):
    # TODO needs to clarify the difference
    # between homepage and upcoming_events?
    return _events_list(request, [])


def events_for_year(request, year):
    events = Event.objects.filter(start__year=year)
    return _events_list(request, events)


def events_for_month(request, year, month):
    events = Event.objects.filter(start__year=year,
                                  start__month=month)
    return _events_list(request, events)


def events_for_day(request, year, month, day):
    events = Event.objects.filter(start=date(int(year), int(month), int(day)))
    return _events_list(request, events)


def _events_list(request, events):
    context = {'events': events}
    return render(request, 'events/events.html', context)


def event(request, event_id):
    ev = Event.objects.get(id=event_id)
    if ev:
        context = {'event': ev}
    else:
        raise Http404
    return render(request, 'events/event.html', context)


class EventViewSet(viewsets.ModelViewSet):
    """API endpoint for events
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer