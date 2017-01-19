import json
import pprint
import os

import tweepy

CONSUMER_TOKEN = os.getenv('TWEEPY_CONSUMER_TOKEN')
CONSUMER_SECRET = os.getenv('TWEEPY_CONSUMER_SECRET')
ACCESS_CREDS_FILE = 'access.creds'


def get_access_creds():
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print "everything sucks and I can't get a request token..."
        raise
    print "Ok, go here, and then tell me your PIN:"
    print redirect_url
    verifier = raw_input('PIN:')
    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print "everything sucks and I can't get an access token..."
        raise
    print "My access token is: %s" % auth.access_token
    print "I will save this token (and secret) to %s" % ACCESS_CREDS_FILE

    with open(ACCESS_CREDS_FILE, 'w') as credsfile:
        credsdict = {'access_token': auth.access_token,
                     'access_token_secret': auth.access_token_secret}
        json.dump(credsdict, credsfile)

auth = tweepy.OAuthHandler(consumer_key=CONSUMER_TOKEN,
                           consumer_secret=CONSUMER_SECRET)

if os.path.exists(ACCESS_CREDS_FILE):
    print 'found %s! attempting to load access creds' % ACCESS_CREDS_FILE
    try:
        credsfile = open(ACCESS_CREDS_FILE)
        credsdict = json.load(credsfile)
        auth.set_access_token(credsdict['access_token'],
                              credsdict['access_token_secret'])
    except ValueError:
        print 'problem with creds file! requesting new creds'
        get_access_creds()
else:
    get_access_creds()

print "Sending a tweet..."

try:
    api = tweepy.API(auth)
    mystatus = api.update_status('tweepy-weepy!  another tweet with python')
except tweepy.TweepError:
    print 'everything sucks and i can\'t tweet'
    print 'access token: %s' % auth.access_token
    print 'access token secret: %s' % auth.access_token_secret
    raise


print "got back status:"
pprint.pprint(mystatus)



print "AND IM SPENT"