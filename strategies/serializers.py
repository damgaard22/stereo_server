from rest_framework import serializers
from alerts.serializers import AlertSerializer
from strategies.models import Strategy


class StrategySerializer(serializers.ModelSerializer):
    alerts = AlertSerializer(many=True)

    class Meta:
        model = Strategy
        fields = ('name', 'alerts')
