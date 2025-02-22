from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.quotes.views import QuoteViewSet

router = DefaultRouter()
router.register(r'quotes', QuoteViewSet, basename='quote')

urlpatterns = [
    path('', include(router.urls)),
]
