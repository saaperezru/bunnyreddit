import requests
import simplejson
from requests.auth import HTTPBasicAuth

class RedditPost:

    def __init__(self,title,url,name):
        self.title = title
        self.url = url
        self.name = name

class RedditAPI:

    def __init__(self,url):
        self.reddit_url = url

    def getPost(self,name):
        req = requests.post(self.reddit_url+'/by_id/'+name+'.json',
           verify=False)
        req.headers['User-Agent'] =  'bunnyreddit/0.1 by saaperezru'
        if(len(simplejson.loads(req.text)['data']['children'])<1):
            raise Exception("No post found by name" + name)
        data = simplejson.loads(req.text)['data']['children'][0]['data']
        return RedditPost(data['title'],data['url'],data['name'])

    def getTrending(self,channel,number,sort='hot'):
        req = requests.post(self.reddit_url+'/r/'+ channel  +'/' + sort + '.json',
           data={
                'limit': number,
                'show': 'all'
           }, 
           verify=False)
        req.headers['User-Agent'] =  'bunnyreddit/0.1 by saaperezru'
        data = simplejson.loads(req.text)
        print data
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

    def getRead(self,bid):
        req = requests.get(self.bunny_url+'/reads/'+bid,
            auth=HTTPBasicAuth(self.api_id, self.api_key),verify=False)
        data = simplejson.loads(req.text)
        return data['reads'][0]['urls']['part001']['original']
