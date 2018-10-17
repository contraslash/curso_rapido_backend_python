

from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response

from . import (
    serializers,
    utils,
    conf
)

# Create your views here.


class Register(GenericAPIView):

    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.Register

    def post(self, request, *args, **kwargs):
        response = dict()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            jwt_user = utils.create_jwt_token_for_user(user)
            response.update(
                {
                    "status": conf.STATUS_OK,
                    "message": conf.USER_CREATED_MESSAGE,
                    "response": jwt_user
                }
            )
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response.update(
                {
                    "status": conf.STATUS_BAD,
                    "message": conf.USER_NOT_CREATED_MESSAGE,
                    "response": serializer.errors
                }
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class LogIn(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.LogIn

    def post(self, request, *args, **kwargs):
        response = dict()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            jwt_user = utils.create_jwt_token_for_user(serializer.user)
            response.update(
                {
                    "status": conf.STATUS_OK,
                    "message": conf.LOGIN_SUCCEED_MESSAGE,
                    "response": jwt_user
                }
            )
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response.update(
                {
                    "status": conf.STATUS_BAD,
                    "message": conf.LOGIN_FAILED_MESSAGE,
                    "response": serializer.errors
                }
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class Verify(GenericAPIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        response = dict()
        authorization = request.META.get("HTTP_AUTHORIZATION", "")
        authorization = authorization.replace("JWT ", "")
        if utils.token_is_valid(authorization):
            response.update(
                {
                    "status": conf.STATUS_OK,
                    "message": conf.TOKEN_VALID,
                    "response": dict()
                }
            )
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response.update(
                {
                    "status": conf.STATUS_BAD,
                    "message": conf.TOKEN_INVALID,
                    "response": dict()
                }
            )
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)