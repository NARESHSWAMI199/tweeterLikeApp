from django.db import models
import random
from django.db.models import Q 
from django.conf import settings





User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet",on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True,null=True)



# here we can apply direct query here and make our view looking cleaner and preety
class TweetQuerySet(models.QuerySet):
    def feed(self,user):
        profile_exist = user.following
        profiles = user.following.all()
        followed_users_id = []
        if profile_exist:
            # here we used the flat argumetn beacuse we need just only user_id
            followed_users_id = user.following.filter(user__id = user.id)#user.following.vlaues_list("user__id",flat=True)
        # get users id which following the our profile
        # distinct deny the duplicate values. we need beacuse the in query we have or function as "Q" keywrod

        # here self represent the  //   Model.objects
        return self.filter(Q(user__id__in=followed_users_id) | Q(user = user)).distinct().order_by("-timestamp")

# we can manage our data as for a function or according your afficient way
class TweetManager(models.Manager):
    # this method is predifind in Manager Class
    def get_queryset(self,*arg,**kwargs):
        return  TweetQuerySet(self.model,using=self._db)

    # we need to create this function for call and provide the user into the feed function
    #  here this function calling the uppder QuerySet Class's funciton 

    # if you calling this function here you don't need to do the use all() method queryset anothrer you need
    def feed(self,user):
        return self.get_queryset().feed(user)

# we need some history for user for extra you cam remove this but for i added



class Tweet(models.Model): 
    # we need a parent class for retweet for same tweet so we use same table for retweet
    parent = models.ForeignKey("self",null= True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    content = models.TextField(null=True,blank=True)
    # you must add a realted name beacuse you have user as Forenkey and in likes
    # using likes m2m we enter data in TweetLike table or model
    likes = models.ManyToManyField(User,related_name='tweet_user',through=TweetLike)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True)

    # adding a new filed
    objects = TweetManager()


    # def __str__(self):
    #     return self.content

    # get id in desending order for last item in firt postion or you can say reverse
    class Meta:
        ordering = ['-id']


    # this is will a boolean vlaue which tell we that if user== None then this is not a retweet else tweet
    @property
    def is_retweet(self):
        return self.parent != None

# feel free to delete
    def senterlize(self):
        context = {
            'id': self.id,
            'content':self.content,
            'likes' : random.randint(0,200)
        }
        return context


