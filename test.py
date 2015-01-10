import requests
import simplejson
from requests.auth import HTTPBasicAuth

bunny_url = 'https://api.voicebunny.com'
reddit_url = 'https://api.voicebunny.com'
api_id = '41789'
api_key = "e7675939164ae130c817ab067d4ca7dd"


def sendProj(title,script,test=1):
    req = requests.post(bunny_url+'/projects/addSpeedy',
       data={
            'title': title,
            'script': script,
            'test': test
       }, 
       auth=HTTPBasicAuth(api_id, api_key),verify=False)
    data = simplejson.loads(req.text)
    return data['project']


def getProj(bid):
    req = requests.get(bunny_url+'/reads/'+bid,
        auth=HTTPBasicAuth(api_id, api_key),verify=False)
    data = simplejson.loads(req.text)
    return data['reads'][0]['urls']['part001']['original']

def getTrending(number):
    req = requests.get(reddit_url+'/r/hot.json',verify=False)
    data = simplejson.loads(req.text)
    return data[]
