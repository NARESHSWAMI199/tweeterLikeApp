from django.contrib import admin
from django.urls import path
from tweets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name="home"),
    path('tweet/',views.item_json_list, name="tweet"),
    path('create-tweet/',views.tweet_create_view, name="create-tweet"),

]
