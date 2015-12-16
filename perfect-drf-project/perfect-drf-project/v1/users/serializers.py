from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text

from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

# Get the UserModel
User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def save(self, *args, **kwargs):
        """create user
        """
        User.objects.create_user(**self.validated_data)
    '''
    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        username = data.get('username', None)
        if username:
            raise serializers.ValidationError({'a': 55, 'b': 99})
        return data
    '''
    '''
    def to_internal_value(self, data):
        """
        """
        #validity = self.is_valid()
        #import pdb; pdb.set_trace();

        #if data['start'] > data['finish']:
        #    raise serializers.ValidationError("finish must occur after start")
        return data
    '''
    def to_representation(self, obj):
        """Delete important info, for instance, password
        """
        ret = super(SignUpSerializer, self).to_representation(obj)
        ret.pop("password", None)
        return ret
