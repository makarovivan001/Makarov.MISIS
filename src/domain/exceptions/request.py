from rest_framework.exceptions import APIException
from rest_framework import status


class MethodNotAllowedException(APIException):
    status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    detail = 'Метод не поддерживается'