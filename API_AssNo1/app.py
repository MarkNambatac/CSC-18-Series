

import json
import oauth2

# Application Settings
consumer_key = "rNP6vrSOh2DEvEgzKkfYNLehZ"
consumer_secret = "13CjYe8t2elQaGvZaWjtzsKBCo9Ui4J3Xwjp7owOLvcJkW3Dgw"

# Access Tokens
access_token = "965961232262971392-ciDm7oTBbilKMsNqL9ZL79fPtJyHVeW"
access_token_secret = "rZp96hJafF08Mbr0283oWdBRBp2hfsL9lAvCZNzMwCl8W"

consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
access_token = oauth2.Token(key=access_token, secret=access_token_secret)
client = oauth2.Client(consumer, access_token)

show_status_format = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=botmark36&count="


def view_tweets():
    while True:
        try:
            num_tweets = int(input("How many tweets do you want to view from your profile? "))
        except ValueError:
            print("That was not a valid number. Try again")
            continue
        else:
            break

    response, data = client.request(show_status_format + str(num_tweets))
    tweets = json.loads(data)

    for tweet in tweets:
        print("These are your tweet/s for the past few days")
        print("Created at : " + tweet['created_at'])
        print("Tweet: " + tweet['text'])

view_tweets()