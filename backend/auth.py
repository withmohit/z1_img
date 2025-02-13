from fastapi import APIRouter, Request
import tweepy
import os

router = APIRouter()

API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
CALLBACK_URL = "http://localhost:8000/auth/callback"  # Change for production

@router.get("/auth/login")
def login():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET, CALLBACK_URL)
    redirect_url = auth.get_authorization_url()
    return {"redirect_url": redirect_url}

@router.get("/auth/callback")
def callback(request: Request):
    oauth_token = request.query_params.get("oauth_token")
    oauth_verifier = request.query_params.get("oauth_verifier")

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.request_token = {"oauth_token": oauth_token, "oauth_token_secret": oauth_verifier}

    access_token, access_token_secret = auth.get_access_token(oauth_verifier)

    return {"access_token": access_token, "access_token_secret": access_token_secret}
