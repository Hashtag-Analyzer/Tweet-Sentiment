import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features

def getData(user, pw, doc):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username=user,
        password=pw)
    url = 'https://gateway.watsonplatform.net/natural-language-understanding/api'
    response = natural_language_understanding.analyze(
        text=doc,
        features=[features.Sentiment(), features.Emotion()])
    return json.dumps(response)
