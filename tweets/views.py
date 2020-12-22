import random
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

 
def home_view(request,*args,**kwargs):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request,"tweets/hello.html")

def tweets_list_view(request,*args,**kwargs):
    return render(request,"tweets/list.html")

def tweets_detail_view(request,tweet_id,*args,**kwargs):
    print("the tweet id " ,tweet_id)
    return render(request,"tweets/detail.html",context={'tweet_id':tweet_id})

def tweet_create_view_with_pure_djagno(request,*args,**kwargs):
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({},status=401)
        return redirect(LOGIN_URL)

    form = TweetForm(request.POST or None)
    next_url = request.POST.get('url')

    # check a url submiting from form post method and redirect there
    # for checking is ajax request or not this wirrten false so we set some header in sending form
    # print('is ajax ; ', request.is_ajax())
    if form.is_valid():
        # this will save form data in your memory and you need a action for save in database
        obj = form.save(commit=False)
        # do other from related logic
        obj.user = user
        obj.save()

        # here we same thing we saving the obj class data
        form = TweetForm()

        if request.is_ajax():
            return JsonResponse( obj.senterlize() , status= 201)  # // we send this when we create something

        # Here i using is_safe_url which is send the same host which you allowed in setting else don't rediect
        # simple mean you can't redirect   http://google.com 
        if next_url !=None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
    if form.errors:
        if request.is_ajax():  
            return JsonResponse( form.errors , status= 400) 
        
    return render(request ,'componants/forms.html', context={'form':form})


def item_json_list_with_pure_djagno(request,*args,**kwargs):
    tweets = Tweet.objects.all()
    tweet_list = [i.senterlize()  for i in tweets]
    
    data = {
        'response' : tweet_list
    }
    return JsonResponse(data ,status = 200)  # the status is a response form server wich get xhr 


def tweet_detail_list_with_pure_django( request,tweet_id ):
    data = {}
    status = 200
    try:
        obj = Tweet.objects.get( id = tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = ['not found']
        status = 401
    return JsonResponse(data ,status=401)



    