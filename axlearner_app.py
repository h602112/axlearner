from flask import Flask, request
from flask import render_template
from search import youtube_search
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = Flask(__name__)

f = open('/home/rocotics/WebDev/yt_key', 'r')
DEVELOPER_KEY = f.read()
youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    
    # Append 'guitar lesson' to the query if it's not already present
    if 'guitar lesson' not in query.lower():
        query += ' guitar lesson'
        
    response = youtube.search().list(
        q=query, type='video', part='id,snippet', maxResults=10
    ).execute()
    videos = [{
        'title': item['snippet']['title'],
        'videoId': item['id']['videoId']
    } for item in response['items']]
    return render_template('results.html', videos=videos)
    
