from users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from users.serializers import UserSerializer
from users.permissions import IsCollaboratorOrOwner


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaboratorOrOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"
