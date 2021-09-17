import json
from googleapiclient.discovery import build
import google_auth_oauthlib.flow
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
client_secrets_file = 'youtube-api-key.json'


flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow.run_console()
yt = build('youtube', 'v3', credentials=credentials)


request = yt.playlists().list(part='snippet,contentDetails',maxResults=5,mine=True)
response = request.execute()


