from django.db import models
from django.conf import settings

# we are going to use django signals beause we need to find the url user in predifind Login Tables
from django.db.models.signals import post_save

# Create your models here.

User = settings.AUTH_USER_MODEL



class FollowReation(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestmap = models.DateTimeField(auto_now_add=True)



 
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=220,null=True,blank=True)
    bio = models.TextField(blank=True,null=True)
    # this return the value which database save time
    timestmap = models.DateTimeField(auto_now_add=True)
    # this is return the present time
    update = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(User,related_name='following',blank=True)

    '''
    project_obj = Profile.objects.first()
    project_obj.followers.all() -> All users following this profile
    user.following.all() ->  All  users profiles I follow

    '''

# this function recives the singnals form User
# this is a predifind function in django
def user_did_save(sender,instance,created,*args,**kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

post_save.connect(user_did_save,sender=User)

# after the user logs in -> verify profile