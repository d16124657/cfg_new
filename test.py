import tweepy

CONSUMER_KEY = 'QmQVv24NlZK6zfcXVhs3eRonI'
CONSUMER_SECRET = 'X5ECsiXx5RyOaz7MKJfruA7qYFZJirpTNi46Vx5TRjLpZ21tPR'
ACCESS_TOKEN = '983668790385954816-54D6eO25786X1QxDlPUth1sgsIBlU8K'
ACCESS_TOKEN_SECRET = 'Y0NqjUeBPLFU48ZGU7gWOnXVm3nYepGTknm1olzeI2bWf'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#status = "Testing!"
#api.update_status(status=status)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
#tweet = 'Hello, world!'
#api.update_status(status=tweet)