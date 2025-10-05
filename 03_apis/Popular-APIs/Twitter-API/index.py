import tweepy

#print(dir(tweepy))

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
my_tweets = api.user_timeline()
for t in my_tweets:
    print(t.text)
    
# getting a particluar user's tweets
user = api.get_user('kvlly')
user.screen_name
user.name

for t in tweets:
    print(t.text)