CONSUMER_KEY = 'T6juvyiQgcB4fIt3WUV5tjUq2'
CONSUMER_SECRET = 'NQDzlwjF7bQYk5MOdeZp6NsdMRAehL916CsP87iqyAC92OZd24'
ACCESS_KEY = '2346369812-iiNNtF5qarI641KnkI31bF0hdQ2XAO5VdcMHcgV'
ACCESS_SECRET = 'hpG2njU6t8beWPJujLrFrQqUzdIaiTPe5DU8KlL6Ltss9'
import tweepy
print('This is my TwitterBot')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions= api.mentions_timeline()

for mention in mentions:
     print(str(mention.id)+'-'+mention.text)
     if '#helloworld' in mention.text.lower():
         print('Found')