from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class LoginViewSet(ViewSet):
    def login(self, request: Request) -> Response:
        username = request.data.get("login")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Нет такого пользователя"}, status=status.HTTP_403_FORBIDDEN)


class LogoutViewSet(ViewSet):
    def logout(self, request: Request) -> Response:
        logout(request)
        return Response({}, status=status.HTTP_200_OK)
