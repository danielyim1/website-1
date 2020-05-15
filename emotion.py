import os
import requests
import json

# Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
# This key will serve all examples in this document.
KEY = os.environ['FACE_SUBSCRIPTION_KEY']

def getEmotion(image_url):
    face_api_url = 'https://emojidetector.cognitiveservices.azure.com/face/v1.0/detect'
    headers = {'Ocp-Apim-Subscription-Key': KEY}

    params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'emotion',
    }

    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image_url})
    print(json.dumps(response.json()))
    return response.json()[0]['faceAttributes']['emotion']

EMOJIKEY = os.environ['EMOJIKEY']  
def getEmoji(feeling):
    emoji_url = "https://emoji-api.com/emojis"
    params = {
        'access_key': EMOJIKEY, 
        'search': feeling
    }
    response = requests.get(emoji_url,params=params)
    emojis = []
    for item in response.json():
        character = item['character'] 
        emojis.append(character)
    return emojis