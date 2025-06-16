import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
import json


load_dotenv()

api_key = os.getenv("YOUTUBE_API_KEY")

REGION = "US"
MAX_RESULTS = 50

#Fetched all trending youtube ids

def get_trending_video_ids(api_key, region, max_results=20):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.videos().list(
        part="snippet",
        chart="mostPopular",
        regionCode=region,
        maxResults=max_results
    )

    response = request.execute()
    video_ids = [item['id'] for item in response['items']]
    print("Trending Video IDs:")
    for vid in video_ids:
        print(f"https://www.youtube.com/watch?v={vid}")

    return video_ids

if __name__ == "__main__":
    trending_ids = get_trending_video_ids(api_key, REGION, MAX_RESULTS)

    print("\nVIDEO_IDS = ", trending_ids)

    with open("video_ids.json", "w") as f:
        json.dump(trending_ids, f, indent=2)
    
