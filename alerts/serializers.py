from rest_framework import serializers
from alerts.models import Alert


class AlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alert
        fields = (
            'public_id',
            'symbol',
            'relative_volume',
            'volume',
            'price',
            'time',
            'date',
            'change',
            'float',
            'gap_dollars',
            'gap_percentage',
            'strategy'
        )

