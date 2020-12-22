from django.contrib import admin
from .models import Tweet,TweetLike




class TweetLikeAdmin(admin.TabularInline):
    model = TweetLike

class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikeAdmin]
    list_display = ['content','user']
    search_fields = ['user__username','user__email' ,'user__id','content']

    class Meta:
        model = Tweet


admin.site.register(Tweet,TweetAdmin) 
admin.site.register(TweetLike) 

