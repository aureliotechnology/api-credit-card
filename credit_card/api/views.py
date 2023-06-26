from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from credit_card.models import CreditCard
from .serializers import CreditCardSerializer

class ReadOnlyCreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

    def get_actions(self):
        actions = super().get_actions()
        del actions['update']
        del actions['partial_update']
        del actions['destroy']
        return actions

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')


class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer