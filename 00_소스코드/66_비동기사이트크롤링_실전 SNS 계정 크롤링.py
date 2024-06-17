import requests
import json
import boto3
from urllib import parse

s3 = boto3.resource('s3')
screen_name = 'Marvel'
tweets = []

headers = {    
    'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'cookie': 'personalization_id="v1_c2W/JlFoXOTVMDmEq5kq+A=="; guest_id_marketing=v1%3A163801789548699633; guest_id_ads=v1%3A163801789548699633; guest_id=v1%3A163801789548699633; ct0=1c48741401762bf1e1385bb64ddd8782; gt=1464579446057619463; _ga=GA1.2.1363300174.1638017926; _gid=GA1.2.1982388954.1638017926; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE%2FyjvSFlFJR45yIlYF%2Bw%3D%3D; g_state={"i_p":1638025146386,"i_l":1}',
    'referer': 'https://twitter.com/BTS_twt',
    'sec-ch-ua': 'Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'x-csrf-token': '1c48741401762bf1e1385bb64ddd8782',
    'x-guest-token': '1464579446057619463',
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ko'
}

params = {
    'variables': '{"screen_name":"' + screen_name + '","withSafetyModeUserFields":true,"withSuperFollowsUserFields":true}'
}

url = 'https://twitter.com/i/api/graphql/7mjxD3-C6BxitPMVQ6w0-Q/UserByScreenName'

response = requests.get(url, params=params, headers=headers)
rest_id = response.json()['data']['user']['result']['rest_id']

url = 'https://twitter.com/i/api/graphql/oFye9u4wTHv8E7oec5UaLA/UserTweets'

params = {
    "userId": rest_id,
    "count": 20,
    "withTweetQuoteCount": True,
    "includePromotedContent": True,
    "withQuickPromoteEligibilityTweetFields": False,
    "withSuperFollowsUserFields": True,
    "withUserResults": True,
    "withBirdwatchPivots": False,
    "withDownvotePerspective": False,
    "withReactionsMetadata": False,
    "withReactionsPerspective": False,
    "withSuperFollowsTweetFields": True,
    "withVoice": True,
    "withV2Timeline": False
}

params_text = json.dumps(params)
params_text = parse.quote(params_text)
response = requests.get(url + '?variables=' + params_text, headers=headers)
response_json = response.json()

for tweet in response_json['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries']:
    try:
        tweets.append({
            'full_text': tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'],
            'user_id_str': tweet['content']['itemContent']['tweet_results']['result']['legacy']['user_id_str']
        })
    except:
        pass

cursor = response_json['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries'][-1]['content']['value']

for i in range(10):

    params = {
        "userId": rest_id,
        "count": 20,
        "cursor": cursor,
        "withTweetQuoteCount": True,
        "includePromotedContent": True,
        "withQuickPromoteEligibilityTweetFields": False,
        "withSuperFollowsUserFields": True,
        "withUserResults": True,
        "withBirdwatchPivots": False,
        "withDownvotePerspective": False,
        "withReactionsMetadata": False,
        "withReactionsPerspective": False,
        "withSuperFollowsTweetFields": True,
        "withVoice": True,
        "withV2Timeline": False
    }

    params_text = json.dumps(params)
    params_text = parse.quote(params_text)
    response = requests.get(url + '?variables=' + params_text, headers=headers)
    response_json = response.json()

    for tweet in response_json['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries']:
        try:
            tweets.append({
                'full_text': tweet['content']['itemContent']['tweet_results']['result']['legacy']['full_text'],
                'user_id_str': tweet['content']['itemContent']['tweet_results']['result']['legacy']['user_id_str']
            })
        except:
            pass

    cursor = response_json['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries'][-1]['content']['value']
    
s3.Bucket('study-012314').put_object(Key=f'tweet_user/{screen_name}.json', Body=json.dumps(tweets, ensure_ascii=False))
print('완료')