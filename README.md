== Configure ==

Register on voicebunny and get some credit assigned to your account. Then go to http://voicebunny.com/api-for-voice-overs/token and copy the API id and token to the bunnyreddit/settings.py file variables:

 * BUNNY_API_ID
 * BUNNY_API_KEY

== Deploy instructions ==

Make sure you have both Python and virtualenv installed and then execute:

```
virtualenvenv ./
source ./bin/activate
pip install -r req.txt
cd bunnyreddit/
python manage.py migrate
python manage.py flush #Answer yes to the question to start the app from scratch
python manage.py syncdb 
python manage.py runserver
```
