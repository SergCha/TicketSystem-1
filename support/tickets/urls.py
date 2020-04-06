from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from tickets.views import home


from . import views

urlpatterns = [
    path('<uuid:uuid>/', views.get_ticket_by_uuid),
    path('add/', views.post_new_ticket),
    path('', views.home, name='home'),
    path('', views.check, name='check'),
    path('', views.faq, name='faq'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
