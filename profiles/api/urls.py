from django.contrib import admin
from django.urls import path
from profiles.api import views

'''
END POINT  /api/profiles/
'''

urlpatterns = [
    path('user/<str:username>/',views.profile_detail_api_view),
    path('<str:username>/follow/',views.profile_detail_api_view),
]
    