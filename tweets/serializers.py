from django.conf import settings
from rest_framework import serializers
from profiles.serializers import ProfileSerailizers
from .models import Tweet

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
ACTIONS_LIST = ['Like','Unlike','Retweet']





class TweetActionsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True,required=False)
    

    def validate_actions(self,value):
        value = value.lower() # Like - > like
        if not vlaue in ACTIONS_LIST:
            raise(serializers.ValidationError("this is not a valid action"))
        return value




class TweetCreateSerializer(serializers.ModelSerializer):
    user = ProfileSerailizers(source='user.profile',read_only=True)
    likes  = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tweet
        fields = ['user',
                    'id',
                    'content',
                    'likes',
                    'timestamp'
                    ]

    def get_likes(self,obj):
        return obj.likes.count()
    
    # def get_user(self,obj):
    #     return obj.user.id 

    # the serializer need self value of fields not recommand self.content
    def validate_content(self,value):  
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError('the tweet is so long')
        return value

# this is for retweet 
class TweetSerializer(serializers.ModelSerializer):
    user = ProfileSerailizers(source='user.profile',read_only=True)
    # if you this  validation then you must use get method
    likes  = serializers.SerializerMethodField(read_only=True)
    liked_count  = serializers.SerializerMethodField(read_only=True)
    # this not the parent objects of the Tweet class this orignal Tweet or self Tweet class 
    parent = TweetCreateSerializer(read_only=True)

    # we don't have the content validation here beacuse we can tweet create a delete and edit here not only delete

    class Meta:
        model = Tweet
        fields = ['user',
                    'id',
                    'content',
                    'likes',
                    'liked_count',
                    'parent',
                    'timestamp'
                    ]

    def get_likes(self,obj):
        return obj.likes.count()
    


    # this user liked these post we can get this using relatedname same we using following
    def get_liked_count(self,obj):
        return obj.user.tweet_user.count()





