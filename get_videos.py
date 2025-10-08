import requests
import pandas as pd
import get_videos_content
from dotenv import load_dotenv
import os
import geminic
import datetime

load_dotenv()

def create_dataframe(videos_info):
    df = pd.DataFrame(videos_info)
    df.to_excel("dados.xlsx", index=False)

def get_videos():
    url = os.getenv("URL_SEARCH")
    params = {"key": os.getenv("KEY"), "part": "snippet", "order": "relevance", "q": "contra reforma agrária", "type": "video", "maxResults": 2}

    response = requests.get(url, params)

    response = (response.json()['items'])
    videos_info = []
    video = {'title':'', 'description':'', 'publishedAt':'','channelId': '', 'channelTitle':'', 'videoId': '', 'viewCount': '', 'likeCount': '', 'contentDescription':'', 'collectionDate': '', 'url': ''}

    for video_info in response:
        video['title'] = video_info["snippet"]['title']   
        video['description'] = video_info["snippet"]['description']
        video['publishedAt'] = video_info["snippet"]['publishedAt']
        video['channelId'] = video_info["snippet"]['channelId']
        video['videoId'] = video_info["id"]['videoId']
        video['channelTitle'] = get_videos_content.get_video_author_channel_name(video['videoId'])
        video['viewCount'] = get_videos_content.get_video_viewCount(video['videoId'])
        video['likeCount'] = get_videos_content.get_video_likeCount(video['videoId'])
        video['contentDescription'] = geminic.get_video_content_description(video['title'])
        video['collectionDate'] = datetime.datetime.now()
        video['url'] = "www.youtube.com/watch?v=" + video['videoId']
        videos_info.append(video)
        print(video)
        video = {'title':'', 'description':'', 'publishedAt':'','channelId': '', 'channelTitle':'', 'videoId': '', 'viewCount': '', 'likeCount': '', 'contentDescription':'', 'collectionDate': '', 'url': ''}
    create_dataframe(videos_info)
    
get_videos()