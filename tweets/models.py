from django.db import models
import random
from django.conf import settings



User = settings.AUTH_USER_MODEL





# we need some history for user for extra you cam remove this but for i added

class TweetLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet",on_delete=models.CASCADE)
    timestmap = models.DateTimeField(auto_now_add=True,null=True)




class Tweet(models.Model): 
    # we need a parent class for retweet for same tweet so we use same table for retweet
    parent = models.ForeignKey("self",null= True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    content = models.TextField(null=True,blank=True)
    # you must add a realted name beacuse you have user as Forenkey and in likes
    # using likes m2m we enter data in TweetLike table or model
    likes = models.ManyToManyField(User,related_name='tweet_user',through=TweetLike)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    timestmap = models.DateTimeField(auto_now_add=True,null=True)


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


