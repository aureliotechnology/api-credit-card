from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReadOnlyCreditCardViewSet

router = DefaultRouter()
router.register(r'', ReadOnlyCreditCardViewSet, basename='creditcard')

urlpatterns = [
    path('', include(router.urls)),
]
