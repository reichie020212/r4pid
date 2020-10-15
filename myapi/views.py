from abc import ABC
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from django.contrib.auth import login
from . import serializers
from myapi.models import Triangle
from myapi.models import Square
from myapi.models import Rectangle
from myapi.models import Diamond


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, *args, **kwargs)


class RegistrationView(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        serializer = serializers.RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            password = serializer.validated_data.get('password')
            user.set_password(password)
            user.save()
            return Response(
                'User has been created',
                status=status.HTTP_200_OK,
            )
        return Response(
            {'error': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class APIBaseView(
    GenericAPIView,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    ABC,
):

    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = None
    model = None

    def get_queryset(self):
        return self.model.objects.all()

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except AssertionError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk') or None
            if pk:
                return Response('Remove pk in the URL.', status=status.HTTP_400_BAD_REQUEST)
            return self.create(request, *args, **kwargs)
        except AssertionError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            return Response({
                "Area": self.object.calculate_area(),
                "Perimiter": self.object.calculate_perimeter(),
            })
        except AssertionError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except AssertionError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response("Object successfully deleted", status=status.HTTP_200_OK)


class TriangleAPIView(APIBaseView):
    serializer_class = serializers.TriangleSerializer
    model = Triangle


class SquareAPIView(APIBaseView):
    serializer_class = serializers.SquareSerializer
    model = Square


class RectangleAPIView(APIBaseView):
    serializer_class = serializers.RectangleSerializer
    model = Rectangle


class DiamondAPIView(APIBaseView):
    serializer_class = serializers.DiamondSerializer
    model = Diamond
