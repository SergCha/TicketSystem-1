import uuid as uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class SupportOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Ticket(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.TextField()
    body = models.TextField()
    reporter_email = models.EmailField()
    reporter_name = models.TextField()

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

    created_at = models.DateTimeField(default=now())
    changed_at = models.DateTimeField(null=True)
    changed_by = SupportOfficer()


class Reactions(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    body = models.TextField()

    created_at = models.DateTimeField(default=now())
    changed_at = models.DateTimeField(null=True)
    changed_by = SupportOfficer()


