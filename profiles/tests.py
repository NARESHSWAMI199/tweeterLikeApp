from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile
from rest_framework.test import APIClient


# here you can demo testing for your code

User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self,*args,**kwargs):
        self.user = User.objects.create_user(username='manish',password='somepassword')
        self.userb = User.objects.create_user(username="king",password="kingisking")


    # this is imported form django_rest_framework which is a thrid part api
    # checking user login or not
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        # we have two users and checking that two profiles are created or not
        self.assertEqual(qs.count(),2)

    def test_following(self):
        first = self.user
        second = self.userb
        first_profile = first.profile.followers.add(second) # added a follower
        second_user_following_whom = second.following.all()
        # here the followers realted name is following
        qs = second.following.filter(user=first) # from a user check the user following which user  
        self.assertTrue(qs.exists())
        # reverse of this
        fist_user_following_no_one = first.following.all()  
        # if query is not exists
        self.assertFalse(fist_user_following_no_one.exists())

    def test_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(f"/api/profiles/{self.userb.username}/follow/",
            {"action":"follow"}
        )
        r_data = response.json()
        count = r_data.get('count')
        self.assertEqual(count,1)



    def test_unfollow_api_endpoint(self):
        first = self.user
        second = self.userb
        first_profile = first.profile.followers.add(second) # added a follower

        # unfollow a user 

        client = self.get_client()
        response = client.post(f"/api/profiles/{self.userb.username}/follow/",
            {"action":"unfollow"}
        )
        r_data = response.json()
        count = r_data.get('count')
        self.assertEqual(count,0)



    def test_cannot_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(f"/api/profiles/{self.user.username}/follow/",
            {"action":"follow"}
        )
        r_data = response.json()
        count = r_data.get('count')
        self.assertEqual(count,0)

