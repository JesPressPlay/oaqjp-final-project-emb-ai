import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    # Get into nested structure to reach the 5 emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    #Pull each score out by key

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # The dominant emotion, aka the key with the highest score
    dominant_emotion = max(emotions, key=emotions.get)

    # Return required output format
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy.
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }