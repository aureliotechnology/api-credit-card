from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .view import HomeView
from django.urls import path, include


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('credit-card/', include('credit_card.api.urls'))
]
