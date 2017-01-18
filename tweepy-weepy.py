import os

import tweepy

CONSUMER_TOKEN = os.getenv('TWEEPY_CONSUMER_TOKEN')
CONSUMER_SECRET = os.getenv('TWEEPY_CONSUMER_SECRET')


auth = tweepy.OAuthHandler(consumer_key=CONSUMER_TOKEN,
                           consumer_secret=CONSUMER_SECRET)


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

print "Sending a tweet..."

api = tweepy.API(auth)

mystatus = api.update_status('tweepy-weepy!  tweeting with python')

print "got back status %s" % mystatus



print "AND IM SPENT"