import requests
import pandas as pd

url = "https://www.googleapis.com/youtube/v3/videos"

def get_video_viewCount(video_id):
    params = {"key": "AIzaSyAtjHKIdUaHRAUQseIhqow0Wl4a3eKBnT8", "part": "statistics", "id": video_id}
    response = requests.get(url, params).json()
    return(response["items"][0]["statistics"]["viewCount"])

def get_video_likeCount(video_id):
    params = {"key": "AIzaSyAtjHKIdUaHRAUQseIhqow0Wl4a3eKBnT8", "part": "statistics", "id": video_id}
    response = requests.get(url, params).json()
    if("likeCount" not in response["items"][0]["statistics"]):
        return "-"
    return (response["items"][0]["statistics"]["likeCount"])