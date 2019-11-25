from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:uuid>/', views.get_ticket_by_uuid),
    path('add/', views.post_new_ticket),
]
