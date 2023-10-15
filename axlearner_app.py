from flask import Flask
from flask import render_template
from search import youtube_search

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', youtube_search=youtube_search)
    
@app.route('/about')
def about():
    return render_template('about.html')
