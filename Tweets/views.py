from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse

from .models import *
# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello Sohan </h1>")

def tweet_details_view(request, tweet_id, *args, **kwargs):

    """
    REST API VIEW
    return JSON data
    """

    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)
    # return HttpResponse(f"<h1> Hello {tweet_id} - {obj.content} </h1>")