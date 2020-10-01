from flask import Flask, render_template
from twitter_filter import StreamListener
from tweet_store import TweetStore

app = Flask(__name__)
store = TweetStore()

@app.route('/')
def index():
    stream_listener = StreamListener()
    stream_listener.start_stream()
    tweets = store.tweets()
    return render_template('index.html', tweets = tweets)

if __name__ == '__main__':
    app.run(debug=True)