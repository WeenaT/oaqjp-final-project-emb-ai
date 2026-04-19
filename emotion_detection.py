# Task 3: Task 3: Format the output of the application

import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   
 
    # Create the data (payload) to send to the API
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
   
    # Set required headers for the API
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
   
    # Send a POST request to the API
    response = requests.post(url, json=myobj, headers=header)
   
    # 1. Convert JSON text to dictionary
    formatted_response = json.loads(response.text)

    # 2. Extract emotion scores
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    # 3. Determine dominant emotion
    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    #4. Return required format
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }

    # Return formatted response
    return {
        "dominant_emotion": dominant_emotion,
        "score": score
    }

