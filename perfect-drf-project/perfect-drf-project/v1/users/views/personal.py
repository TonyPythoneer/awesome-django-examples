from django.contrib.auth import get_user_model

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from api_root.authentications.auth import ExpiringTokenAuthentication
from ..serializers.personal import UserDetailSerializer, AboutMeSerializer


# Get the UserModel
User = get_user_model()


class AboutMeView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns User's details in JSON format.
    Accepts the following GET parameters: token
    Accepts the following POST parameters:
        Required: token
        Optional: email, first_name, last_name and UserProfile fields
    Returns the updated UserProfile and/or User object.
    """
    authentication_classes = (ExpiringTokenAuthentication,)
    serializer_class = AboutMeSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserDetailView(generics.RetrieveAPIView):
    """
    Returns User's details in JSON format.
    Accepts the following GET parameters: token
    Accepts the following POST parameters:
        Required: token
        Optional: email, first_name, last_name and UserProfile fields
    Returns the updated UserProfile and/or User object.
    """
    queryset = User.objects.all()
    authentication_classes = (ExpiringTokenAuthentication,)
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)
