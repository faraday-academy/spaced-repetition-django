# /cards /cards/:id
from django.urls import path, include
from rest_framework import routers
from .views import CardsViewSet

router = routers.DefaultRouter()
router.register(r'', CardsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
