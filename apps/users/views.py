from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from .serializers import UserSerializer
@extend_schema(
    summary="User Registration",
    description="Creates a new user account.",
    request=UserSerializer,
    responses={
        201: {
            "example": {
                "status": "success",
                "data": {
                    "id": 1,
                    "username": "newuser",
                    "email": "newuser@example.com"
                },
                "message": "User registered successfully. Please log in to get your token."
            }
        },
        400: {
            "examples": [
                {
                    "status": "error",
                    "message": "Validation error",
                    "errors": None
                }
            ]
        }
    },
)
class RegisterUserView(generics.CreateAPIView):
    """
    API to register a new user (without returning a token).
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "status": "error",
                    "message": "Validation error",
                    "errors": serializer.errors if request.user.is_staff else None,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = serializer.save()

        return Response(
            {
                "status": "success",
                "data": serializer.data,
                "message": "User registered successfully. Please log in to get your token."
            },
            status=status.HTTP_201_CREATED,
        )