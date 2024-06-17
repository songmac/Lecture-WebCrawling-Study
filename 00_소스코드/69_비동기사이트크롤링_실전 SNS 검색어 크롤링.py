import requests
import boto3
import json

tweets = []
s3 = boto3.resource('s3')
search_text = '스파이더맨'

headers = {
    'accept': '*/*',
    #'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cookie': 'personalization_id="v1_c2W/JlFoXOTVMDmEq5kq+A=="; guest_id_marketing=v1%3A163801789548699633; guest_id_ads=v1%3A163801789548699633; guest_id=v1%3A163801789548699633; ct0=1c48741401762bf1e1385bb64ddd8782; _ga=GA1.2.1363300174.1638017926; _gid=GA1.2.1982388954.1638017926; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE%2FyjvSFlFJR45yIlYF%2Bw%3D%3D; gt=1464624757488627713; g_state={"i_p":1638115602959,"i_l":2}',
    'referer': 'https://twitter.com/search?q=%EB%A9%94%ED%83%80%EB%B2%84%EC%8A%A4&src=typed_query&f=live',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'x-csrf-token': '1c48741401762bf1e1385bb64ddd8782',
    'x-guest-token': '1464624757488627713',
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ko',
}

params = {
    'include_profile_interstitial_type': 1,
    'include_blocking': 1,
    'include_blocked_by': 1,
    'include_followed_by': 1,
    'include_want_retweets': 1,
    'include_mute_edge': 1,
    'include_can_dm': 1,
    'include_can_media_tag': 1,
    'include_ext_has_nft_avatar': 1,
    'skip_status': 1,
    'cards_platform': 'Web-12',
    'include_cards': 1,
    'include_ext_alt_text': True,
    'include_quote_count': True,
    'include_reply_count': 1,
    'tweet_mode': 'extended',
    'include_entities': True,
    'include_user_entities': True,
    'include_ext_media_color': True,
    'include_ext_media_availability': True,
    'include_ext_sensitive_media_warning': True,
    'send_error_codes': True,
    'simple_quoted_tweet': True,
    'q': search_text,
    'tweet_search_mode': 'live',
    'count': 20,
    'query_source': 'typed_query',
    'pc': 1,
    'spelling_corrections': 1,
    'ext': 'mediaStats,highlightedLabel,voiceInfo,superFollowMetadata'
}

response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=headers, params=params)
response_json = response.json()

for tweet in response_json['globalObjects']['tweets']:
    tweets.append({
        'full_text': response_json['globalObjects']['tweets'][tweet]['full_text'],
        'user_id': response_json['globalObjects']['tweets'][tweet]['user_id']
    })
    
cursor = response_json['timeline']['instructions'][0]['addEntries']['entries'][-1]['content']['operation']['cursor']['value']

for i in range(10):

    params = {
        'include_profile_interstitial_type': 1,
        'include_blocking': 1,
        'include_blocked_by': 1,
        'include_followed_by': 1,
        'include_want_retweets': 1,
        'include_mute_edge': 1,
        'include_can_dm': 1,
        'include_can_media_tag': 1,
        'include_ext_has_nft_avatar': 1,
        'skip_status': 1,
        'cards_platform': 'Web-12',
        'include_cards': 1,
        'include_ext_alt_text': True,
        'include_quote_count': True,
        'include_reply_count': 1,
        'tweet_mode': 'extended',
        'include_entities': True,
        'include_user_entities': True,
        'include_ext_media_color': True,
        'include_ext_media_availability': True,
        'include_ext_sensitive_media_warning': True,
        'send_error_codes': True,
        'simple_quoted_tweet': True,
        'q': search_text,
        'tweet_search_mode': 'live',
        'count': 20,
        'query_source': 'typed_query',
        'cursor': cursor,
        'pc': 1,
        'spelling_corrections': 1,
        'ext': 'mediaStats,highlightedLabel,voiceInfo,superFollowMetadata'
    }

    response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=headers, params=params)
    response_json = response.json()

    for tweet in response_json['globalObjects']['tweets']:
        tweets.append({
            'full_text': response_json['globalObjects']['tweets'][tweet]['full_text'],
            'user_id': response_json['globalObjects']['tweets'][tweet]['user_id']
        })
        
    cursor = response_json['timeline']['instructions'][-1]['replaceEntry']['entry']['content']['operation']['cursor']['value']

s3.Bucket('study-012314').put_object(Key=f'tweet_search/{search_text}.json', Body=json.dumps(tweets, ensure_ascii=False))
print('완료')