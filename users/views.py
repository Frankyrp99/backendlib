from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from users.serializers import UserSerializer, AuthTokenSerializer
from users.models import User


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class RetriveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
