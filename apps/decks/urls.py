# /decks /decks/:id
# /decks/:id/cards
from django.urls import path, include
from rest_framework_nested import routers
from .views import DecksViewSet, CardsViewSet, TodaysCardsViewSet

router = routers.SimpleRouter()
router.register(r'', DecksViewSet)

cards_router = routers.NestedSimpleRouter(router, r'', lookup='decks')
cards_router.register(r'cards', CardsViewSet, basename='deck_cards')

todays_cards_router = routers.NestedSimpleRouter(router, r'', lookup='decks')
todays_cards_router.register(r'todays-cards', TodaysCardsViewSet, basename='todays_cards')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls)),
    path('', include(todays_cards_router.urls)),
]
