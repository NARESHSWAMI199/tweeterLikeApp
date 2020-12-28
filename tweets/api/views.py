import random
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.utils.http import is_safe_url
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
# the rest_framework Response similler to  from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from django.conf import settings
from ..models import Tweet
from rest_framework.pagination import PageNumberPagination
from ..forms import TweetForm
from ..serializers import (TweetSerializer,
                            TweetActionsSerializer,
                            TweetCreateSerializer)


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

@api_view(['GET'])
# we create a user session with using SessionAuthentication classes from rest_frame work
# @authentication_classes([SessionAuthentication]) # at that time we don't need beacuse rest_framework defalut has a sesion
@permission_classes([IsAuthenticated])
def tweet_detail_list( request,tweet_id ):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({},status=401)
    serializer = TweetSerializer(qs[0])
    return Response(serializer.data , status=200)


# defalut paginatation
def get_paginated_queryset_response(qs,request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    # here feed is a custom method i have difind in models.py
    paginator_qs = paginator.paginate_queryset(qs,request)
    # we can pass a context in serialzers and get in this serizlizers class
    serializer = TweetSerializer(paginator_qs,many=True,context={"request":request})
    # if you have a pagination then you be send a paginataion respose and this don't have any status
    return paginator.get_paginated_response(serializer.data)




@permission_classes([IsAuthenticated])
@api_view(['GET'])
# here we have more way to do this but we working here for clearty
def tweet_feed_view(request,*args,**kwargs):
    user = request.user
    # here feed is a custom method i have difind in models.py
    qs = Tweet.objects.feed(user)
    # this function is defind just up side of this function
    return get_paginated_queryset_response(qs,request)# return Response(serializer.data ,status=200)




@api_view(['GET'])
def item_json_list(request,*args,**kwargs):
    qs = Tweet.objects.all()
    username = request.GET.get('username')
    if username !=None:
        qs = qs.filter(user__username__iexact =username)
    return get_paginated_queryset_response(qs,request)


 
 
@api_view(['POST'])  #this can take a list as args for check for what method you allow to this 
@permission_classes([IsAuthenticated])
def tweet_create_view(request , *args,**kwargs):
    # you msut need add the data keyword here  or don't need to request.POST or None afte api_view verification
    serializer = TweetCreateSerializer(data = request.data)
    # we can sent the actual error threw serailzers
    if serializer.is_valid( raise_exception= True ):
        # save the data more eaist way comapare to django ModelForm 
        serializer.save(user=request.user)
        return Response(serializer.data, status = 201)  
    return Response({}, status = 400)
    
# Tweet Delete View
@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view( request,tweet_id ):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({},status=401)  
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({'Message' : "you can't delete this tweet"},status=401)
    obj = qs.first()
    obj.delete()
    return Response({'Message': 'tweet removed'}, status=200)




# tweet_like_view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view( request,*args,**kwargs):
    # for these thinks we need a serializer
    '''
    id is required . 
    Action option are : like ,unlike , retweet 
    
    '''
    # we also write request.data for that time beacuse in this view get
    # data in json format form hello.html
    serializer = TweetActionsSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get('id')
        action= data.get('action')
        content = data.get('content')

    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({},status=401)
    obj = qs.first()

    if action == "like":
        obj.likes.add(request.user)
        serializer = TweetSerializer(obj)
        return Response(serializer.data, status=200)
    elif action == 'unlike': 
        obj.likes.remove(request.user)
        serializer = TweetSerializer(obj)
        return Response(serializer.data,status=200)
    elif action == 'retweet':
        new_tweet = Tweet.objects.create(
            user = request.user,
            parent = obj,
            content = content
        )
        # for send the data 
        new_serializer = TweetSerializer(new_tweet)
        return Response(new_serializer.data,status=201)
    return Response({ }, status=200)



 


    