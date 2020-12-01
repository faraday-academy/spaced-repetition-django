from datetime import date

from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework.response import Response

from .models import Deck
from apps.cards.models import Card
from apps.cards.views import CardsSerializer


class DecksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'title', 'description',
                  'created_at', 'updated_at')


class DecksViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DecksSerializer


class CardsViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk):
        queryset = Card.objects.filter(deck=decks_pk)
        serializer = CardsSerializer(queryset, many=True)
        return Response(serializer.data)


class TodaysCardsViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk):
        """
        Users can get the list of cards from a deck that they
        need to study today.
        This should include cards from previous dates that were
        not studied yet.
        """
        today = date.today()
        queryset = Card.objects.filter(deck=decks_pk,
                        next_review_at__lt=today)
        serializer = CardsSerializer(queryset, many=True)
        return Response(serializer.data)
