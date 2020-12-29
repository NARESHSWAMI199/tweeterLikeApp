from django.contrib import admin
from django.urls import path
from .views import (profile_detail_view,
                    update_profile_view)

app_name = 'profiles'
urlpatterns = [
    path('edit/',update_profile_view),
    path('<str:username>/',profile_detail_view),
]
