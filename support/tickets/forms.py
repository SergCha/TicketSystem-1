from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('subject', 'body', 'reporter_email', 'reporter_name')