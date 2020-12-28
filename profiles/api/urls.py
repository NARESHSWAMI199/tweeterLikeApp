from django.contrib import admin
from django.urls import path
from profiles.api import views

'''
END POINT  /api/profiles/
'''

urlpatterns = [
    path('<str:username>/follow/',views.user_following_view),
    path('user/<str:username>/',views.profile_detail_api_view),
]
    