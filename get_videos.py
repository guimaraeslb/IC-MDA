import requests
import pandas as pd
import get_videos_content

def create_dataframe(videos_info):
    df = pd.DataFrame(videos_info)
    df.to_excel("dados.xlsx", index=False)

def get_videos():
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {"key": "AIzaSyAtjHKIdUaHRAUQseIhqow0Wl4a3eKBnT8", "part": "snippet", "order": "relevance", "q": "contra reforma agrária", "type": "video", "maxResults": 40}

    response = requests.get(url, params)

    response = (response.json()['items'])
    videos_info = []
    video = {'title':'', 'description':'', 'channelTitle': '', 'videoId': '', 'viewCount': '', 'likeCount': ''}

    for video_info in response:
        video['title'] = video_info["snippet"]['title']   
        video['description'] = video_info["snippet"]['description']
        video['channelTitle'] = video_info["snippet"]['channelTitle']
        video['videoId'] = video_info["id"]['videoId']
        video['viewCount'] = get_videos_content.get_video_viewCount(video['videoId'])
        video['likeCount'] = get_videos_content.get_video_likeCount(video['videoId'])
        videos_info.append(video)
        video = {'title':'', 'description':'', 'channelTitle': '', 'videoId': '', 'viewCount': '', 'likeCount': ''}
    create_dataframe(videos_info)

get_videos()