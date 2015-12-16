from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import SignUpSerializer


User = get_user_model()


class SignUpView(generics.CreateAPIView):
    """
    """
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save()

'''
class UserDetailViewSet(mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    Returns User's details in JSON format.
    Accepts the following GET parameters: token
    Accepts the following POST parameters:
        Required: token
        Optional: email, first_name, last_name and UserProfile fields
    Returns the updated UserProfile and/or User object.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
'''