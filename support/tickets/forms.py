from django.forms import ModelForm

from tickets.models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['reporter_name', 'reporter_email', 'subject', 'body']
