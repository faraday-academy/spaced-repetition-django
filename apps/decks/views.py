from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import Deck


class DecksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'title', 'description')


class DecksViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DecksSerializer
