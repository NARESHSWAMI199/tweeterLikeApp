import random
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.utils.http import is_safe_url
from .models import Tweet
from .forms import TweetForm
from django.conf import settings

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request,*args,**kwargs):
    return render(request,"tweets/hello.html")



def tweet_create_view(request,*args,**kwargs):
    form = TweetForm(request.POST or None)
    # check a url submiting from form post method and redirect there
    next_url = request.POST['url']


    if form.is_valid():
        # this will save form data in your memory and you need a action for save in database
        obj = form.save(commit=False)
        # do other from related logic
        obj.save()
        # here we same thing we saving the obj class data
        form = TweetForm()
        # Here i using is_safe_url which is send the same host which you allowed in setting else don't rediect
        # simple mean you can't redirect   http://google.com 
        if next_url !=None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        context = {
            'form':form
        }
    return render(request ,'componants/forms.html', context)


def item_json_list(request,*args,**kwargs):
    tweets = Tweet.objects.all()
    tweet_list = [ {'id': i.id , 'content' : i.content , 'likes':random.randint(0,12535) }  for i in tweets]
    
    data = {
        'response' : tweet_list
    }
    return JsonResponse(data ,status = 400)