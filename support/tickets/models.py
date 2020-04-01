import uuid as uuid

from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User
from django.db import models


class SupportOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class TicketStatus(models.Model):
    STATE_CHOICES = [
        ('NE', 'New'),
        ('PR', 'Processed'),
        ('SL', 'Solved'),
        ('CL', 'Closed'),
    ]

    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default='NE',
    )


class Ticket(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.TextField()
    body = models.TextField()
    reporter_email = models.EmailField()
    reporter_name = models.TextField()

    state = AutoOneToOneField(TicketStatus, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey('SupportOfficer', on_delete=models.DO_NOTHING, default=None, null=True, blank=True)


class Reactions(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    state = AutoOneToOneField(TicketStatus, on_delete=models.CASCADE)
    body = models.TextField()
    officer = models.ForeignKey('SupportOfficer', default=None, null=True, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey('Reactions', on_delete=models.DO_NOTHING, null=True)


