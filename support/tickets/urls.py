from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:uuid>/', views.get_ticket_by_uuid),
    path('add/', views.post_new_ticket),
    path('', views.home, name='home'),
    path('', views.send, name='send'),
    path('', views.check, name='check'),
    path('', views.faq, name='faq'),
]
