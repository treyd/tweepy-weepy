import json
import pprint
import os

import tweepy

CONSUMER_TOKEN = os.getenv('TWEEPY_CONSUMER_TOKEN')
CONSUMER_SECRET = os.getenv('TWEEPY_CONSUMER_SECRET')
ACCESS_CREDS_FILE = 'access.creds'


auth = tweepy.OAuthHandler(consumer_key=CONSUMER_TOKEN,
                           consumer_secret=CONSUMER_SECRET)


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


def exit_menu(api):
    return False


def my_stats(api):
    apiuser = api.me()
    print "User %s (%s)" % (apiuser.name, apiuser.screen_name)
    print "Tweets: %d" % apiuser.statuses_count
    print "Followers: %d" % apiuser.followers_count
    return True


def list_tweets(api):
    return


def wipe_timeline(api):
    return


MENU_CHOICES = (
    (1, 'my stats', my_stats),
    (2, 'list tweets', list_tweets),
    (3, 'wipe timeline', wipe_timeline),
    (9, 'quit', exit_menu)
)


def handle_choice(choice):
    for menuchoice in MENU_CHOICES:
        if int(choice) == menuchoice[0]:
            return menuchoice[2]


def main_menu(api):
    apiuser = api.me()
    print "welcome %s" % apiuser.screen_name
    print "main menu:"
    for menuchoice in MENU_CHOICES:
        print "    %s: %s" % (menuchoice[0], menuchoice[1])
    choice = raw_input('choice: ')

    return handle_choice(choice)(api)


def main():
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

    try:
        api = tweepy.API(auth)

    except tweepy.TweepError:
        print "everything sucks!!"
        print "access token: %s" % auth.access_token
        print "access token secret: %s" % auth.access_token_secret
        raise

    choice = ''

    while main_menu(api):
        pass

    print "byeee"


if __name__ == '__main__':
    main()
