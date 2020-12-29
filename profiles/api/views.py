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
from ..models import Profile
from django.contrib.auth import  get_user_model
from ..serializers import ProfileSerailizers

User = get_user_model()


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


# @api_view(['GET'])  #this can take a list as args for check for what method you allow to this 
# @permission_classes([IsAuthenticated])
# def user_profile_detail_view(request ,username, *args,**kwargs):
#     current_user = request.user
#     to_follow_user  = ??

#     return Response({}, status = 200)






@api_view(['GET','POST'])
def profile_detail_api_view(request,username,*args,**kwargs):
    # get the profile for the user passed username
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        return Response({"profile":"User not found"},status=404)
    profile_obj = qs.first()      
    # we can pass a context in serialzers and get in this serizlizers class
    serializer = ProfileSerailizers(instance = profile_obj,context={'request': request}) 
    # data = {}
    # try :
    #     data = request.data
    # except:
    #     pass 
    # you can write same thing like this
    data = request.data or {}
    if request.method == "POST":
        me = request.user
        print(data)
        action = data.get('action')
        if profile_obj.user != me:
            if action == "follow":
                profile_obj.followers.add(me)
            elif action =="unfollow":
                profile_obj.followers.remove(me)
            else:
                pass
    
    return Response(serializer.data,status=200)





# @api_view(['GET','POST'])  #this can take a list as args for check for what method you allow to this 
# @permission_classes([IsAuthenticated])
# def user_following_view(request ,username, *args,**kwargs):
#     me = request.user
#     other_user_qs  = User.objects.filter(username=username)
#     # simple mean user can't follow self
#     if me.username == username:
#         my_followers = me.profile.followers.all()
#         return Response({"count": my_followers.count()},status= 200)
        
        
#     if not other_user_qs.exists():
#         return Response({}, status = 404)
#     other = other_user_qs.first()
#     profile = other.profile
#     data = {}
#     try :
#         data = request.data
#     except:
#         pass

#     print(data)
#     action = data.get('action')
#     if action == "follow":
#         profile.followers.add(me)
#     elif action =="unfollow":
#         profile.followers.remove(me)
#     else:
#         pass
#     data = ProfileSerailizers(instance = profile,context={'request': request})  
#     return Response(data.data,status=200)


