from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index(request: WSGIRequest) -> render:
    return render(request, 'lending/index.html')