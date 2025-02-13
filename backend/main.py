from fastapi import FastAPI, UploadFile, File, HTTPException
from image_processing import process_images
from twitter_api import post_images_to_twitter
import os

app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        resized_images = process_images(file)
        return {"message": "Images resized", "files": list(resized_images.keys())}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/post/")
async def post_images():
    try:
        result = post_images_to_twitter()
        return {"message": "Images posted successfully", "details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
