from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    session = 0
    random = get_random_string(length=32)
    if session == 0:
        return random
    session += 1
    return(request, "index.html", random)