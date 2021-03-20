from apps.soporte.api import ListTickets
from django.conf.urls import url

urlpatterns = [
    url(r'^list/$', ListTickets.as_view(), name='list_tickets'),
]
