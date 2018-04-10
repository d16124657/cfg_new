import time
import tweepy


CONSUMER_KEY = 'QmQVv24NlZK6zfcXVhs3eRonI'
CONSUMER_SECRET = 'X5ECsiXx5RyOaz7MKJfruA7qYFZJirpTNi46Vx5TRjLpZ21tPR'
ACCESS_TOKEN = '983668790385954816-54D6eO25786X1QxDlPUth1sgsIBlU8K'
ACCESS_TOKEN_SECRET = 'Y0NqjUeBPLFU48ZGU7gWOnXVm3nYepGTknm1olzeI2bWf'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



#starting account
account="careylu2018"


user = api.get_user(account)  #give detailed information on user and its followers/following (only 20 per call)

#info on the owner of the account
print (user.screen_name)
print (user.followers_count)
print (user.friends_count)

#info on the first 20 friends
for friend in user.friends():
   print(friend.screen_name)
   print(friend.followers_count)
   print(friend.friends_count)

#info on the first 20 followers
for friend in user.followers():
   print(friend.screen_name)
   print(friend.followers_count)
   print(friend.friends_count)

#if you are calling get_user many times, add a waiting time with the instruction:  time.sleep(10)  #the number inside parenthesis are seconds
