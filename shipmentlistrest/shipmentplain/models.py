from django.db import models


class Shipment(models.Model):
    shipmentId = models.CharField(max_length=10)
    weight = models.FloatField()
    volume = models.FloatField()
    shipmentType = models.CharField(max_length=10)
    invoiceNumber = models.CharField(max_length=10)
    shipTo = models.CharField(max_length=100)
    shipFrom = models.CharField(max_length=100)

    def __str__(self):
        return self.shipmentId
