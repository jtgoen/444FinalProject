import json

rise_up_october = open('../../Downloads/RiseUpOctober.json', 'r')

users = {}
tweets = {}
hashtags = {}
for line in rise_up_october:
    tweet = json.loads(line)
    user_field = tweet['user']
    if user_field['id_str'] not in users:
        users[user_field['id_str']] = {
            'name': user_field['name'],
            'screen_name': user_field['screen_name'],
            'tweets': [],
            'num_followers': user_field['followers_count']
        }

    # Construct tweet object
    tiny_tweet = {
        'text': tweet['text'],
        'timestamp': tweet['created_at'],
        'hashtags': [],
        'num_retweets': tweet['retweet_count']
    }
    for hashtag in tweet['entities']['hashtags']:
        tiny_tweet['hashtags'].append(hashtag['text'])
        if hashtag['text'] not in hashtags:
            hashtags[hashtag['text']] = 1
        else:
            hashtags[hashtag['text']] += 1

    users[user_field['id_str']]['tweets'].append(tweet['id_str'])
    tweets[tweet['id_str']] = tiny_tweet

rise_up_users = open('rise_up_users.json', 'w')
rise_up_tweets = open('rise_up_tweets.json', 'w')
rise_up_hashtags = open('rise_up_hashtags.json', 'w')

rise_up_users.write(json.dumps(users, indent=2, separators=(',', ': ')))
rise_up_tweets.write(json.dumps(tweets, indent=2, separators=(',', ': ')))
rise_up_hashtags.write(json.dumps(hashtags, indent=2, separators=(',', ': ')))
