from rest_framework import serializers
from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = '__all__'

    def validate_shipmentId(self, value):
        query_set = Shipment.objects.filter(shipmentId__iexact=value)
        if self.instance:
            query_set = query_set.exclude(pk=self.instance.pk)
        if query_set.exists():
            raise serializers.ValidationError("Shipment Id / tracking no. must be unique")
        return value
