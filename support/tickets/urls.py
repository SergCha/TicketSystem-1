from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:uuid>/', views.get_ticket_by_uuid),
    path('add/', views.post_new_ticket),
    path('', views.home, name='post-new'),
    path('check/', views.check, name='check'),
    path('check/search/', views.search_ticket),
]
