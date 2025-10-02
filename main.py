import requests

url = "https://www.googleapis.com/youtube/v3/videos"
params = {'key':'AIzaSyAtjHKIdUaHRAUQseIhqow0Wl4a3eKBnT8','part': "snippet", "chart":"mostPopular", 'regionCode': 'BR'}
response = requests.get(url, params=params)

videos = response.json()["items"]
videos_info = []

for video in videos:
    print(video["snippet"])