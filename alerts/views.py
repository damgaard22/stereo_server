from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, pagination, serializers, filters
from alerts.serializers import AlertSerializer
from alerts.models import Alert
from datetime import datetime

# Create your views here.


class AlertsViewSet(mixins.CreateModelMixin,
             mixins.ListModelMixin,
             viewsets.GenericViewSet):

    serializer_class = AlertSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['-time']

    def get_queryset(self):
        queryset = Alert.objects.all()

        strategy = self.request.query_params.get('strategy', None)
        date = self.request.query_params.get('date', None)
        time = self.request.query_params.get('time', None)

        try:
            if strategy:
                queryset = queryset.filter(strategy__name=strategy)

            if date:
                date = datetime.strptime(date, "%d-%m-%Y")
                queryset = queryset.filter(date=date)

            if time:
                time = datetime.strptime(time, "%H:%M:%S")
                queryset = queryset.filter(time__lte=time)

            return queryset

        except:
            raise serializers.ValidationError({'query_param': ['Sent invalid query parameter']})

