from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.soporte.permissions import TicketsPermission
from apps.soporte.serializers import TickeSerializer
from apps.soporte.models import Ticket


class ListTickets(APIView):

    permission_classes = (IsAuthenticated, TicketsPermission,)

    def get(self, request):
        """
        Return a list of all ticket.
        """
        ticket = Ticket.objects.all()
        serializer = TickeSerializer(ticket, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
