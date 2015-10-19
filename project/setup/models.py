from django.db import models
import uuid


class Device(models.Model):
    device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_name = models.CharField(max_length=50, blank=False, null=True)
    friendly_name = models.CharField(max_length=50, blank=False, null=True, unique=True)
    model_name = models.CharField(max_length=50, blank=False, null=True, unique=True)
    description = models.TextField(blank=True, null=True)
    computer = models.ForeignKey('setup.Computer')



class Computer(models.Model):
    computer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CPU = models.TextField(max_length=30, blank=False, null=True, verbose_name="Processor")
    GPU = models.TextField(max_length=40, blank=True, null=True, verbose_name="Graphics Card")
    RAM = models.IntegerField(blank=False, null=True)



class Peripheral(models.Model):
    peripheral_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, blank=False, null=True)
    model_name = models.CharField(max_length=100, blank=False, null=True)
    device = models.ForeignKey('setup.Device')
