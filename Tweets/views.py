from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.http import is_safe_url
from django.http import Http404, HttpResponse, JsonResponse

from .models import *

from .forms import *

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.

def home_view(request, *args, **kwargs):

    return render(request, "Pages/home.html", context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'Components/forms.html', context={'form':form})

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [x.serialize() for x in qs]
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
