from django.contrib import admin

from tickets.models import Ticket, SupportOfficer

admin.site.register(SupportOfficer)
admin.site.register(Ticket)
