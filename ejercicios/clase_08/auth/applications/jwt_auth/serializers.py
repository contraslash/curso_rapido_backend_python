from rest_framework import serializers

from django.contrib.auth import models, authenticate


from . import conf

class Register(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        )

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user

class LogIn(serializers.ModelSerializer):
    _user = None

    @property
    def user(self):
        return self._user

    class Meta:
        model = models.User
        fields = (
            'username',
            'password'
        )

    def is_valid(self, raise_exception=False):
        super(LogIn, self).is_valid(raise_exception)
        print(self.data)
        user = authenticate(**self.data)
        print(user)
        if user is not None:
            self._user = user
            return True
        else:
            self._errors = {
                "all": conf.USERNAME_OR_PASSWORD_INVALID_MESSAGE
            }
            return False