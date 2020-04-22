from django.forms import ModelForm
from django import forms

from tickets.models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['reporter_name', 'reporter_email', 'subject', 'body']

class SearchTicketForm(forms.Form):
    reporter_email = forms.EmailField()
    id_ticket = forms.CharField()