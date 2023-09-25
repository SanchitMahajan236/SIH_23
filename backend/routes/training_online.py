from fastapi import APIRouter
import requests

# API Key
youtube_api_key = "<your-api-key-here>"

router = APIRouter()

# Youtube Headers.
headers = {
    # "Authorization" : "Bearer " + youtube_api_key,
    "Accept" : "application/json"
}

@router.get("/get-channels",tags=["training_online"])
def getChannels():
    # Youtube search query
    query = "odop"

    params={"part":"snippet",
            "q":"odop",
            "type":"channel",
            "key":youtube_api_key}

    # Make API call to Youtube
    resp = requests.get(url="https://www.googleapis.com/youtube/v3/search",
                        headers=headers,
                        params=params)
    return resp.json()

@router.get("/get-videos",tags=["training_online"])
# To get the video link
# `https://www.youtube.com/watch?v=${result.id.videoId}`
def getVideos():
    # Youtube search query
    query = "odop"

    params={"part":"snippet",
            "q":"odop",
            "type":"Videos",
            "key":youtube_api_key}

    # Make API call to Youtube
    resp = requests.get(url="https://www.googleapis.com/youtube/v3/search",
                        headers=headers,
                        params=params)
    return resp.json()
