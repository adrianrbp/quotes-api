from django.urls import path
from apps.quotes.views import QuoteListCreateView

urlpatterns = [
    path("quotes/", QuoteListCreateView.as_view(), name="quote-list"),
]
