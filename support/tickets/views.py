from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from tickets.models import Ticket


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