from django.contrib import admin
from .models import Profile

# Register your models here.
 
class ProfileFollowingDeatail(admin.ModelAdmin):
    list_display = ['user']
    class Meta:
        model = Profile


admin.site.register(Profile,ProfileFollowingDeatail)
