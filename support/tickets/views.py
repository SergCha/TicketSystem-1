from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from tickets.models import Ticket


def home(request):
    return render(request, 'home.html')


def check(request):
    return render(request, 'tickets/check.html')


def get_ticket_by_uuid(request, uuid):
    try:
        ticket = Ticket.objects.get(pk=uuid)
    except Ticket.DoesNotExist:
        raise Http404("Ticket does not exist")
    return render(request, 'tickets/detail.html', {'ticket': ticket})


@require_POST
@csrf_exempt
def post_new_ticket(request):
    print(request.body)
    return render(request, 'home.html')
