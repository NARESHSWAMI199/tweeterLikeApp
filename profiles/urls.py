from django.contrib import admin
from django.urls import path
from .views import (profile_detail_view,
                    update_profile_view)

urlpatterns = [
    path('<str:username>/',profile_detail_view,name="tweets_profile_view"),
    path('edit',update_profile_view)
]
