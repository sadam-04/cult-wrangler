from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Event
from .forms import EventResponseForm


def home(request):
    events = Event.objects.all()
    return render(request, "wrangler/homepage.html", {'events':events})

def event_view(request, eid):
    event = get_object_or_404(Event, uid=eid)
    return render(request, "wrangler/event.html", {'event':event})

def submit_response(request):
    if request.method == 'POST':
        form = EventResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = EventResponseForm()
    return redirect('homeX')