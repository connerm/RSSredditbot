
from flask import Flask, request
import praw
import feedparser
import time
from random import choice

app = Flask(__name__)

#reddit OAuth information - remove for git hosting
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URL = ''

#app for Flask web server
@app.route('/')

#function for retreiving RSS info

#start of app 
def redditbot():
  r.login('user', 'password')
  rss_url = 'http://www.quotationspage.com/data/qotd.rss'; #example rss
  feed = feedparser.parse(rss_url)
  items = feed['items']
  
  #continous loop
  while True:
    subreddit = r.get_subreddit('test')
    subreddit_comments = subreddit.get_comments()
    already_done = []
    for comment in subreddit_comments:
      if comment.id not in already_done:
	item = choice(items)
	message_body = ' ' + item['summary'] + ' - ' + item['title'] + '\n'
	#error in findinf user - couldn't find in documentation
	r.send_message(user, 'A quote for you', message_body)
    time.sleep(600) #10mins
  

if __name__ == '__main__':
  #praw information
  r = praw.Reddit('my bot felix')
  r.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)
  #app for flask
  app.run(debug=True, port=65010)