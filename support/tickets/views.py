from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .models import Ticket, TicketStatus
from .forms import TicketForm

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
        ticketform = TicketForm(request.POST)
        if ticketform.is_valid():
            ticketform.save()
            reporter_name = ticketform.cleaned_data["reporter_name"]
            return HttpResponse("<h2>Hello, {0}</h2>".format(reporter_name))     #вспомогательная строка для контроля записи в БД
        else:
            return HttpResponse("Invalid data")   #вспомогательная строка для контроля записи в БД
    else:
        ticketform = TicketForm()
        return render(request, "home.html", {"ticketform": ticketform})
