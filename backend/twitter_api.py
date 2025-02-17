import os
import tweepy
from fastapi import FastAPI, APIRouter, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# FastAPI App
app = FastAPI()
router = APIRouter()

# CORS Middleware (for frontend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Twitter API credentials
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
CONSUMER_KEY = os.getenv("X_CLIENT_ID")
CONSUMER_SECRET = os.getenv("X_CLIENT_SECRET")

# Debugging: Print API keys (Remove in production)
if not all([ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET]):
    print("❌ Twitter API keys are missing!")

# Authenticate with Tweepy
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


@router.post("/post")
async def post_to_twitter(file: UploadFile = File(...), tweet_text: str = Form("New post from FastAPI!")):
    """
    Upload an image and post it as a tweet on Twitter.
    """
    try:
        # Save file temporarily
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Upload media to Twitter
        media = api.media_upload(filename=file_path)

        # Post tweet with image
        tweet = api.update_status(status=tweet_text, media_ids=[media.media_id])

        # Cleanup: Delete temporary file
        os.remove(file_path)

        return {
            "message": "✅ Tweet posted successfully!",
            "tweet_id": tweet.id_str,
            "tweet_url": f"https://twitter.com/user/status/{tweet.id_str}"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error posting tweet: {str(e)}")


# Add router to FastAPI app
app.include_router(router)
