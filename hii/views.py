from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Hello Skillfacktory")

# Create your views here.
