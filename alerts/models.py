from django.db import models
from strategies.models import Strategy
import uuid
# Create your models here.


class Alert(models.Model):
    public_id = models.UUIDField(editable=False, default=uuid.uuid4)
    symbol = models.CharField(max_length=5)
    relative_volume = models.FloatField(null=True, blank=True)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, related_name='alerts')
    volume = models.PositiveIntegerField()
    price = models.FloatField()
    time = models.TimeField()
    five_min_vol = models.FloatField(null=True, blank=True)
    date = models.DateField()
    gap_dollars = models.FloatField(null=True, blank=True)
    gap_percentage = models.FloatField(null=True, blank=True)
    change = models.FloatField(null=True, blank=True)
    float = models.IntegerField(null=True, blank=True)

    objects = models.Manager()
