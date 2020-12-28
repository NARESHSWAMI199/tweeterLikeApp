from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static  import static
from django.views.generic import TemplateView
from tweets import views
from accounts.views import (
    login_view,
    logout_view,
    register_view
)



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home_view,name='home_view'),
    path('global',views.tweets_list_view,name="tweets_list_view"),
    path('login/',login_view,name="login_view"),
    path('logout/',logout_view,name="logout_view"),
    path('register/',register_view,name="register_view"),

    path('<int:tweet_id>/',views.tweets_detail_view, name="tweets_detail_view"),
    # here i repath beacuse we want profile or profiles both work so i make 's' is optional
    re_path(r'profiles?/', include('profiles.urls')),
    path('api/tweet/', include('tweets.api.urls')),
    re_path(r'api/profiles?/', include('profiles.api.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
