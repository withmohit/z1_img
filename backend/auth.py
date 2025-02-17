import os
from fastapi import APIRouter, HTTPException
import requests
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# Twitter API credentials
CLIENT_ID = os.getenv("X_CLIENT_ID")
CLIENT_SECRET = os.getenv("X_CLIENT_SECRET")
REDIRECT_URI = "https://z1-imgback.onrender.com/auth/callback"

@router.get("/auth/login")
def login():
    """Redirects user to Twitter login."""
    auth_url = (
        f"https://twitter.com/i/oauth2/authorize"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=tweet.read users.read offline.access"
        f"&state=secure_random_string"
        f"&code_challenge=challenge"
        f"&code_challenge_method=plain"
    )
    return {"login_url": auth_url}

@router.get("/auth/callback")
def callback(code: str):
    """Handles Twitter OAuth callback."""
    token_url = "https://api.twitter.com/2/oauth2/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "code_verifier": "challenge"
    }
    response = requests.post(token_url, data=data)

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to authenticate")

    tokens = response.json()
    return {"message": "Authenticated!", "tokens": tokens}
