from django.shortcuts import render
from django.http import Http404, HttpResponse

from .models import *
# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello Sohan </h1>")

def tweet_details_view(request, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f"<h1> Hello {tweet_id} - {obj.content} </h1>")