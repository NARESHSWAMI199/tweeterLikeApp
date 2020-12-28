from django.contrib import admin
from django.urls import path
from tweets.api import views



urlpatterns = [
    path('',views.item_json_list, name="tweet"),
    path('action/',views.tweet_action_view, name="tweet-action"),   
    path('create/',views.tweet_create_view, name="create-tweet"),
    path('<int:tweet_id>/',views.tweet_detail_list, name="tweet-deatail"),
    path('<int:tweet_id>/delete/',views.tweet_delete_view, name="tweet-delete"),
    path('feed/',views.tweet_feed_view),

]
    