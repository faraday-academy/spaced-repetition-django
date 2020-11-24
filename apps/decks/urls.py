# /decks /decks/:id
# /decks/:id/cards
from django.urls import path, include
from rest_framework import routers
from .views import DecksViewSet

router = routers.DefaultRouter()
router.register(r'', DecksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
