import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='e6463e0ddf15729480d20e77deede23c77da12c4')

url = 'https://gateway-a.watsonplatform.net/calls' \
     # '-watson-personality-insights/'
def getSentiment(text):
    sentiment = json.dumps(alchemy_language.sentiment(text=text))
    sentiment = json.loads(sentiment)
    if sentiment['docSentiment']['type'] == 'neutral':
        return 0;
    else:
        return sentiment['docSentiment']['score']
