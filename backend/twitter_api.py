import requests
import os
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")

def post_images_to_twitter():
    image_paths = [f"resized_images/image_{size[0]}x{size[1]}.png" for size in [(300, 250), (728, 90), (160, 600), (300, 600)]]
    
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    media_ids = []

    for path in image_paths:
        with open(path, "rb") as file:
            response = requests.post("https://upload.twitter.com/1.1/media/upload.json", headers=headers, files={"media": file})
            media_ids.append(response.json()["media_id_string"])

    post_url = "https://api.twitter.com/2/tweets"
    tweet_data = {"text": "Resized images", "media": {"media_ids": media_ids}}

    response = requests.post(post_url, headers=headers, json=tweet_data)
    return response.json()
