from rest_framework import serializers
from apps.soporte.models import Ticket

class TickeSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Ticket
        fields = (
            "titulo", "descripcion", "fecha_creacion"
        )
