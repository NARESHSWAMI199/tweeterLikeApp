from django.db import models

class Tweet(models.Model):
    # django have default field it's called id
    # id = models.AutoField(pk= True)
    content = models.TextField()
