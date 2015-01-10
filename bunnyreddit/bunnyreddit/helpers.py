import requests
import simplejson
from requests.auth import HTTPBasicAuth
import logging
import time
logger = logging.getLogger(__name__)

class RedditPost:

    def __init__(self,title,url,name):
        self.title = title
        self.url = url
        self.name = name

class RedditAPI:

    def __init__(self,url,max_attempts=3):
        self.max_attempts = max_attempts
        self.reddit_url = url

    def getPost(self,name):
        error = True
        attempts = 0
        while(error and attempts < self.max_attempts):
            req = requests.post(self.reddit_url+'/by_id/'+name+'.json',
               verify=False)
            req.headers['User-Agent'] =  'bunnyreddit/0.1 by saaperezru'
            data = simplejson.loads(req.text)
            logger.info(data)
            print(data)
            if('error' in data and data['error'] == 429):
                logger.info("Too many requests for reddit!!")
                print("Too many requests for reddit!!")
                time.sleep(5)
            else:
                error = False
            attempts = attempts + 1
        if('error' in data and data['error'] == 429):
            logger.info("Too many requests for reddit!!")
            time.sleep(5)
            raise Exception("No post found by name" + name)
        data = data['data']['children'][0]['data']
        return RedditPost(data['title'],data['url'],data['name'])

    def getTrending(self,channel,number,sort='hot'):
        error = True
        attempts = 0
        while(error and attempts < self.max_attempts):
            req = requests.post(self.reddit_url+'/r/'+ channel  +'/' + sort + '.json',
               data={
                    'limit': number,
                    'show': 'all'
               }, 
               verify=False)
            req.headers['User-Agent'] =  'bunnyreddit/0.1 by saaperezru'
            data = simplejson.loads(req.text)
            print data
            if('error' in data and data['error'] == 429):
                logger.info("Too many requests for reddit!!")
                print("Too many requests for reddit!!")
                time.sleep(5)
            else:
                error = False
            attempts = attempts + 1

        if('error' in data and data['error'] == 429):
            logger.info("Too many requests for reddit!!")
            time.sleep(5)
            raise Exception("Could not get trending")
        ret = []
        for i in data['data']['children']:
            post = i['data']
            ret.append(RedditPost(post['title'],post['url'],post['name']))
        return ret

class BunnyAPI:

    def __init__(self,url,id,key):
        self.bunny_url = url
        self.api_id = id
        self.api_key = key

    def sendProj(self,title,script,test=1):
        req = requests.post(self.bunny_url+'/projects/addSpeedy',
           data={
                'title': title,
                'script': script,
                'test': test
           }, 
           auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data['project']

    def getProject(self,projId):
        req = requests.get(self.bunny_url+'/projects/'+projId,
           auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data

    def getRead(self,bid):
        req = requests.get(self.bunny_url+'/reads/'+bid,
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data
