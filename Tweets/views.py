from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse

from .models import *
# Create your views here.

def home_view(request, *args, **kwargs):

    return render(request, "Pages/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content":x.content, "likes":12} for x in qs]
    data = {
        "isUser": False,
        "response": tweet_list
    }
    return JsonResponse(data)

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
