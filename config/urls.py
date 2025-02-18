
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("apps.quotes.urls")),
    path("api/users/", include("apps.users.urls")),
    path("api/oauth/", include("oauth2_provider.urls", namespace="oauth2_provider")),

    # Swagger Documentation
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
]
