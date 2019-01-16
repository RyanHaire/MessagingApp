from django.shortcuts import render
from django.http import HttpResponse

# chat views.py

def index(request):

    return HttpResponse("Welcome to the chat room.")