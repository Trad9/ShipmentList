# Generated by Django 2.0.5 on 2018-05-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipmentId', models.CharField(max_length=10)),
                ('weight', models.FloatField()),
                ('volume', models.FloatField()),
                ('shipmentType', models.CharField(max_length=10)),
                ('invoiceNumber', models.CharField(max_length=10)),
                ('shipTo', models.CharField(max_length=100)),
                ('shipFrom', models.CharField(max_length=100)),
            ],
        ),
    ]
