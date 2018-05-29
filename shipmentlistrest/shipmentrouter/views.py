from rest_framework import viewsets
from .models import Shipment
from .serializer import ShipmentSerializer


class ShipmentView(viewsets.ModelViewSet):
        queryset = Shipment.objects.all()
        serializer_class = ShipmentSerializer
