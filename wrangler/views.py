from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Event, EventResponse
import json

@login_required
def home(request):
    events = Event.objects.all()
    return render(request, "wrangler/homepage.html", {'events':events})

@login_required
def event_view(request, eid):
    event = get_object_or_404(Event, uid=eid)

    time_scores = {}
    for e in event.times:
        time_scores[e] = 0

    submissions = []
    for er in EventResponse.objects.filter(event_id=eid):
        # ensure number of responses matches number of options
        if len(event.times) != len(json.loads(er.responses)):
            continue

        r_idx = 0
        for r in json.loads(er.responses):
            if (r == True):
                time_scores[event.times[r_idx]] += 1
            r_idx += 1

        resp_data = []
        for d in range(len(event.times)):
            resp_data.append({"time":event.times[d], "response":json.loads(er.responses)[d]})

        submissions.append({"submitter":er.submitter, "event_id":er.event_id, "data":resp_data})

    print("TIMESCORES: " + str(time_scores))

    return render(request, "wrangler/event.html", {'event':event, 'submissions':submissions})

@login_required
def submit_response(request):
    if request.method == 'POST':
        submitter = request.POST.get('submitter')
        event_id = request.POST.get('event')
        event = get_object_or_404(Event, uid=event_id)
        times_raw = []
        for t in event.times:
            times_raw.append(request.POST.get('time-option-' + str(t)))
        
        times_parsed = []
        for t in times_raw:
            if t == "on":
                times_parsed.append(True)
            else:
                times_parsed.append(False)

        # delete any old responses this user already submitted for this event
        EventResponse.objects.filter(submitter=submitter, event_id=event_id).delete()

        if submitter and event_id and event:
            resp = EventResponse.objects.create(submitter=submitter, event_id=event_id, responses=json.dumps(times_parsed))
            messages.success(request, "Response saved!")
        else:
            messages.error(request, "Invalid or missing data!")

    return redirect('home')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'wrangler/login.html')
    return render(request, 'wrangler/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')