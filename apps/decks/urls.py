# /decks /decks/:id
# /decks/:id/cards
from django.urls import path, include
from rest_framework_nested import routers
from .views import DecksViewSet, CardsViewSet

router = routers.SimpleRouter()
router.register(r'', DecksViewSet)

cards_router = routers.NestedSimpleRouter(router, r'', lookup='decks')
cards_router.register(r'cards', CardsViewSet, basename='deck_cards')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls)),
]
