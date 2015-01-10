from django.shortcuts import get_object_or_404, render
from helpers import *
from django.conf import settings

rAPI = RedditAPI(settings.REDDIT_URL)
bAPI = BunnyAPI(settings.BUNNY_URL,settings.BUNNY_API_ID,settings.BUNNY_API_KEY)

def home(request):
    """
    this will render the home page
    :param request:
    :return: home page of the project
    """
    context = {'posts': rAPI.getTrending('all',1)}
    return render(request, 'home.html',context)
def getPostAudio(post):
    data = bAPI.sendProj(post.name,post.title)
    return data['reads'][0]['urls']['part001']['original']
    
def getPost(request,name):
    context = {
        'wav_audio' : '',
        'mp3_audio' : getPostAudio(rAPI.getPost(name))
    }
    return render(request, 'post.html', context)
