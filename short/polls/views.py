from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def index(request, link):
    # return HttpResponseRedirect('google.com')
    return HttpResponse(link)