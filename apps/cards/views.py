from django.shortcuts import render
from rest_framework import viewsets, serializers
from apps.decks.models import Deck
from .models import Card


class CardsSerializer(serializers.ModelSerializer):
    deck = serializers.PrimaryKeyRelatedField(
            queryset=Deck.objects.all())

    class Meta:
        model = Card
        fields = ('id', 'deck', 'question', 'answer',
                  'created_at', 'updated_at')


class CardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardsSerializer
