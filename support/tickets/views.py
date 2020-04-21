from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import TicketForm, SearchTicketForm
from .models import Ticket, TicketStatus


def home(request):
	return render(request, 'home.html')


def check(request):
    return render(request, 'check.html')


def login(request):
    return render(request, 'login.php')


def get_ticket_by_uuid(request, uuid):
    try:
        ticket = Ticket.objects.get(pk=uuid)
    except Ticket.DoesNotExist:
        raise Http404("Ticket does not exist")
    return render(request, 'tickets/detail.html', {'ticket': ticket})


@require_POST
@csrf_exempt
def post_new_ticket(request):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)

        if ticket_form.is_valid():
            ticket_form.instance.state = TicketStatus.objects.create()
            ticket_form.save()
            reporter_name = ticket_form.cleaned_data["reporter_name"]
            return HttpResponse("<h2>Обращение отправлено, {0}</h2>".format(reporter_name))

        return HttpResponse("Invalid data: {}".format("; ".join(ticket_form.errors)))

    ticket_form = TicketForm()
    return render(request, "home.html", {"ticketform": ticket_form})

def search_ticket(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('id_ticket')
        ticket_email = request.POST.get('reporter_email')
        search_ticket_form = get_object_or_404(Ticket, uuid=ticket_id, reporter_email=ticket_email)
    else:
        search_ticket_form = SearchTicketForm()

    return render(request, "search.html", {'form' : search_ticket_form})