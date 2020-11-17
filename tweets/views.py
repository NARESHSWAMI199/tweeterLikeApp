from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Tweet

def home_view(request,*args,**kwargs):
    return render(request,"hello.html")


def item_json_list(request,*args,**kwargs):
    tweets = Tweet.objects.all()
    tweet_list = [ {'id': i.id , 'content' : i.content }  for i in tweets]
    
    data = {
        'response' : tweet_list
    }
    return JsonResponse(data ,status = 400)