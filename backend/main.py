
import tweepy
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from image_processing import process_images
# from twitter_api import post_images_to_twitter
from auth import router as auth_router
from twitter_api import router as twitter_router
import os
from dotenv import load_dotenv

load_dotenv()
# Twitter API credentials
API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


app = FastAPI()

app.include_router(auth_router)
app.include_router(twitter_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        resized_images = process_images(file)
        return {"message": "Images resized", "files": list(resized_images.keys())}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
