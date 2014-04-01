import argparse, ConfigParser, tweepy

def authenticate():
    '''Reads a config file and authenticates with twitter.'''
    config = ConfigParser.RawConfigParser()
    config.read('/home/jessebishop/.pyconfig')
    access_token_key = config.get('Twitter-OAuth', 'ACCESS_TOKEN_KEY')
    access_token_secret = config.get('Twitter-OAuth', 'ACCESS_TOKEN_SECRET')
    consumer_key = config.get('Twitter-OAuth', 'CONSUMER_KEY')
    consumer_secret = config.get('Twitter-OAuth', 'CONSUMER_SECRET')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth, secure=True)
    return api

def tweet(status):
    api = authenticate()
    if len(status) <= 140:
        s = api.update_status(status)
        return s
    else:
        print "Don't be so wordy!"
        return None

    

if __name__ == "__main__":
    # Get the tweet text as an argument
    p = argparse.ArgumentParser(prog="tweet.py", description="Programatically send a tweet!")
    p.add_argument("status", help="The text of the status you would like to send ( < 140 characters please).")
    args = p.parse_args()

    # Tweet
    s = tweet(args.status)
    print s.id
