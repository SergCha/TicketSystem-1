from django.forms import ModelForm
from tickets.models import Ticket, TicketStatus

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['reporter_name', 'reporter_email', 'subject', 'body', 'state']
