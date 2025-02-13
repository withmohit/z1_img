import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

# Load credentials from .env file
API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def post_images_to_twitter():
    image_paths = ["resized_images/image_300x250.png", "resized_images/image_728x90.png", 
                   "resized_images/image_160x600.png", "resized_images/image_300x600.png"]

    media_ids = []
    for path in image_paths:
        upload = api.media_upload(path)
        media_ids.append(upload.media_id_string)

    api.update_status(status="Here are the resized images! 📸", media_ids=media_ids)

    return {"message": "Images posted successfully!", "media_ids": media_ids}
