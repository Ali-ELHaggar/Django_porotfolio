from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, request


def index(request):

    return render(request, 'show.html')