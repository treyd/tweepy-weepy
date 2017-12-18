# tweepy-weepy
do some stuff with the twitter API. what stuff?  well, you can
   * list your stats
   * list your tweets
   * mass delete all your tweets (which is why I made this)

To install, download the code and run `pip install tweepy`

To actually run, you'll need to create an app on Twitter:
   1. Go to https://apps.twitter.com/ and create a new app with Read Write access
   1. Copy the 'Consumer access key' and 'Consumer access secret' strings
   1. Set the environment variables `TWEEPY_CONSUMER_TOKEN` and `TWEEPY_CONSUMER_SECRET` in your environment
   1. Run `python tweepy-weepy.py` and follow the instructions
