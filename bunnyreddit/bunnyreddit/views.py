from django.shortcuts import get_object_or_404, render
from helpers import *
from django.conf import settings
import logging
from bunnyreddit.models import Post
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)

rAPI = RedditAPI(settings.REDDIT_URL)
bAPI = BunnyAPI(settings.BUNNY_URL,settings.BUNNY_API_ID,settings.BUNNY_API_KEY)
print (settings.BUNNY_URL,settings.BUNNY_API_ID,settings.BUNNY_API_KEY)

def home(request):
    """
    this will render the home page
    :param request:
    :return: home page of the project
    """
    context = {'posts': rAPI.getTrending('all',1)}
    return render(request, 'home.html',context)

def getPostAudio(name):
    p = None
    try:
        p = Post.objects.get(name__exact=name)
        logger.info("Retrieved " + name + " from database")
        proj = bAPI.getProject(p.bunny_proj_id)
        print proj
        print proj['reads']
        p.status = proj['reads'][0]['status']
        p.save()
    except ObjectDoesNotExist:
        post = rAPI.getPost(name)
        proj = bAPI.sendProj(post.name,post.title,test=0)
        logger.info(proj)
        projId = proj['id']
        audio = proj['reads'][0]['urls']['part001']['original']
        status = proj['reads'][0]['status']
        p = Post(name=post.name,title=post.title,bunny_proj_id=projId,audio_url=audio,status=status)
        p.save()
    return p
    
def getPost(request,name):
    p = getPostAudio(name)
    context = {
        'wav_audio' : '',
        'title' : p.title,
        'mp3_audio' : p.audio_url,
        'status' : p.status
    }
    return render(request, 'post.html', context)
