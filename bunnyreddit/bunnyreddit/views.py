from django.shortcuts import get_object_or_404, render
from helpers import *
from django.conf import settings
import logging
from bunnyreddit.models import Post
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)

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
    try:
        p = Post.objects.get(name__exact=post.name)
        logger.info("Retrieved " + name + " from database")
    except ObjectDoesNotExist:
        bid = 0
        audio = ""
        ready = False
        while(not ready):
            try:
                data = bAPI.sendProj(post.name,post.title)
                logger.info(data)
                #bid = data['reads'][0]['id']
                #audio = bAPI.getRead(bid)
                audio = data['reads'][0]['urls']['part001']['original']
                #wait for audio to be ready
                ready = True
            except Exception:
                ready = False
        p = Post(name=post.name,bunny_proj_id=bid,audio_url=audio)
        p.save()
    return p.audio_url
    
def getPost(request,name):
    context = {
        'wav_audio' : '',
        'mp3_audio' : getPostAudio(rAPI.getPost(name))
    }
    return render(request, 'post.html', context)
