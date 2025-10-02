import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_video_viewCount(video_id):
    params = {"key": os.getenv("KEY"), "part": "statistics", "id": video_id}
    response = requests.get(url, params).json()
    return(response["items"][0]["statistics"]["viewCount"])

def get_video_likeCount(video_id):
    params = {"key": os.getenv("KEY"), "part": "statistics", "id": video_id}
    response = requests.get(url, params).json()
    if("likeCount" not in response["items"][0]["statistics"]):
        return "-"
    return (response["items"][0]["statistics"]["likeCount"])