from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def brian(request, jmeno):
    return HttpResponse(f'Hello, {jmeno.capitalize()}')