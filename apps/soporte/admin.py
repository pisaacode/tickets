from django.contrib import admin
from apps.soporte.models import Ticket

# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ['titulo', 'descripcion', 'estados', 'fecha_creacion']
    search_fields = ['titulo']
    list_filter = ['estados']
admin.site.register(Ticket, TicketAdmin)