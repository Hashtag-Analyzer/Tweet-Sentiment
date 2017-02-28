import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language_a = AlchemyLanguageV1(api_key='e6463e0ddf15729480d20e77deede23c77da12c4')
alchemy_language_b = AlchemyLanguageV1(api_key='ffba820d5062423ba1ba98f504f0c8f9e728815c')
url = 'https://gateway-a.watsonplatform.net/calls' \
     # '-watson-personality-insights/'
def getSentiment(text):
    sentiment = json.dumps(alchemy_language_a.sentiment(text=text))
    sentiment = json.loads(sentiment)
    return str(sentiment['docSentiment'])

def getEmotion(text):
    emotion = json.dumps(alchemy_language_b.emotion(text=text))
    emotion = json.loads(emotion)
    return str(emotion['docEmotions'])
