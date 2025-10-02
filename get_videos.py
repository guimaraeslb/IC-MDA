import requests
import pandas as pd
import get_videos_content
from dotenv import load_dotenv
import os

load_dotenv()

def create_dataframe(videos_info):
    df = pd.DataFrame(videos_info)
    df.to_excel("dados.xlsx", index=False)

def get_videos():
    url = os.getenv("URL_SEARCH")
    params = {"key": os.getenv("KEY"), "part": "snippet", "order": "relevance", "q": "contra reforma agrária", "type": "video", "maxResults": 40}

    response = requests.get(url, params)

    response = (response.json()['items'])
    videos_info = []
    video = {'title':'', 'description':'', 'channelTitle': '', 'videoId': '', 'viewCount': '', 'likeCount': ''}

    for video_info in response:
        print(video_info["snippet"])
        video['title'] = video_info["snippet"]['title']   
        video['description'] = video_info["snippet"]['description']
        video['channelId'] = video_info["snippet"]['channelId']
        video['videoId'] = video_info["id"]['videoId']
        video['viewCount'] = get_videos_content.get_video_viewCount(video['videoId'])
        video['likeCount'] = get_videos_content.get_video_likeCount(video['videoId'])
        videos_info.append(video)
        video = {'title':'', 'description':'', 'channelTitle': '', 'videoId': '', 'viewCount': '', 'likeCount': ''}
    create_dataframe(videos_info)

get_videos()