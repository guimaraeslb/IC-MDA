import requests
import pandas as pd

def create_dataframe(videos_info):
    df = pd.DataFrame(videos_info)
    df.to_excel("dados.xlsx", index=False)

def getVideos():
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {"key": "AIzaSyAtjHKIdUaHRAUQseIhqow0Wl4a3eKBnT8", "part": "snippet", "order": "relevance", "q": "contra reforma agrária", "type": "video", "maxResults": 40}

    response = requests.get(url, params)

    response = (response.json()['items'])
    videos_info = []
    video = {'title':'', 'description':'', 'channelTitle': '', 'videoId': ''}

    for i in response:
        video['title'] = i["snippet"]['title']   
        video['description'] = i["snippet"]['description']
        video['channelTitle'] = i["snippet"]['channelTitle']
        video['videoId'] = i["id"]['videoId']
        videos_info.append(video)
        video = {'title':'', 'description':'', 'channelTitle': '', 'videoId': ''}
    create_dataframe(videos_info)

def main():
    getVideos()

main()
