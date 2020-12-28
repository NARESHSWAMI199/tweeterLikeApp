from django.test import TestCase
from .models import Tweet
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
# Create your test here
User = get_user_model()

class TweetTestCase(TestCase):

    # this is a prdifind function or a interface
    def setUp(self):
        self.user = User.objects.create_user(username='manish',password='somepassword')
        self.userb = User.objects.create_user(username="king",password="kingisking")
        # for tweet test crating a demo tweet
        Tweet.objects.create(content="this is first" , user=self.user)
        Tweet.objects.create(content="this is first" , user=self.user)
        Tweet.objects.create(content='this is second',user=self.userb)
        self.current_count = Tweet.objects.all().count()


    # we can test our code like not interact with database but a demo envirment for test
    def test_user_created(self):
        self.assertEqual(self.user.username,'manish')
        self.assertEqual(self.userb.username,'king')

    def test_tweet_created(self):
        tweet = Tweet.objects.create(content="my tweet", user=self.user)
        self.assertEqual(tweet.id,4)
        self.assertEqual(tweet.user , self.user)

    
    def get_client(self):
        client = APIClient()
        client.login(username= self.user, password='somepassword')
        return client



    def test_tweets_realated_name(self):
        user = self.user
        # here  tweets is the realted name
        self.assertEqual(user.tweets.count(),2)


    def test_tweet_list(self):
        client = self.get_client()
        response = client.get('/api/tweet/')
        self.assertEqual(response.status_code ,200)
        self.assertEqual(len(response.json()),3)

    def test_action_like(self):
        client = self.get_client()
        response = client.post('/api/tweet/action/' , {'id' :1 , 'action':'like' })
        self.assertEqual(response.status_code ,200)
        self.assertEqual(response.json().get('likes'),1)
        # 
        user = self.user
        # tweetlike_set  this is the standered option for get element if you have table self's forigenkey
        # decode ->   "tweet" is the class name in lowercase and "like" is instance of this class 
        # you can use the related name for a sacific field
        my_like_instance_count = user.tweetlike_set.count()
        self.assertEqual(my_like_instance_count,1)
        # these both are same
        my_related_like_instance_count = user.tweet_user.count()
        self.assertEqual(my_related_like_instance_count,my_like_instance_count)



    def test_action_unlike(self):
        client = self.get_client()
        response = client.post('/api/tweet/action/' , { 'id' :1 , 'action':'like' })
        self.assertEqual(response.json().get('likes'),1)
        response = client.post('/api/tweet/action/' , { 'id' :1 , 'action':'unlike' })
        self.assertEqual(response.status_code ,200)
        self.assertEqual(response.json().get('likes'),0)


    def test_action_retweet(self):
        client = self.get_client()
        current_count = self.current_count
        response = client.post('/api/tweet/action/', 
        { 'id' : 2, 'action':'retweet'} )
        self.assertEqual(response.status_code ,201)
        new_tweet_id = response.json().get('id')
        self.assertEqual(current_count +1,new_tweet_id)
    

    def test_create_api_view(self):
        client = self.get_client()
        request_data = {'content':'this is new tweeet'}
        response = client.post('/api/tweet/create/') 
        self.assertEqual(response.status_code ,201)
        new_tweet_id = response.json().get('id')
        self.assertEqual(self.current_count +1,new_tweet_id)

    def test_detail_api_view(self):
        client = self.get_client()
        response = client.get('/api/tweet/2/') 
        self.assertEqual(response.status_code ,200)
        new_tweet_id = response.json().get('id')
        self.assertEqual(2,new_tweet_id)



    def test_delete_api_view(self):
        client = self.get_client()
        response = client.delete('/api/tweet/1/delete/') 
        self.assertEqual(response.status_code ,200)
        client = self.get_client()
        response = client.delete('/api/tweet/1/delete/') 
        self.assertEqual(response.status_code ,401)
        response = client.delete('/api/tweet/2/delete/') 
        self.assertEqual(response.status_code ,200)
