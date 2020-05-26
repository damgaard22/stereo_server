from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, pagination
from strategies.serializers import StrategySerializer
from strategies.models import Strategy


# Create your views here.

class StrategyViewSet(mixins.CreateModelMixin,
             mixins.RetrieveModelMixin,
             mixins.UpdateModelMixin,
             mixins.ListModelMixin,
             viewsets.GenericViewSet):
    lookup_field = 'name'
    serializer_class = StrategySerializer
    queryset = Strategy.objects.all()
