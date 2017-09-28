from django.views.generic import View
from django.shortcuts import render
from .models import Tweet, User

# Create your views here.
class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Roy"
        return render(request, "base.html", params)

class Profile(View):
    """User Profile reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user
        return render(request, 'profile.html', params)
