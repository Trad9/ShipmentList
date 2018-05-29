from rest_framework import generics
from rest_framework.response import Response
from .models import Shipment
from rest_framework.views import APIView
from .serializer import ShipmentSerializer


class ShipmentListView(APIView):

    def get(self, request):
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data)


class ShipmentItemUpdate(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = ShipmentSerializer

    def get_queryset(self):
        return Shipment.objects.filter(pk=self.kwargs.get('pk'))


class ShipmentItemView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ShipmentSerializer

    def get_queryset(self):
        return Shipment.objects.filter(pk=self.kwargs.get('pk'))



class ShipmentItemCreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = ShipmentSerializer

    def get_queryset(self):
        return Shipment.objects.filter(pk=self.kwargs.get('pk'))
