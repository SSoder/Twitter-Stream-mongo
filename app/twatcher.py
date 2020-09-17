from flask import Flask, render_template
from tweet_store import TweetStore

app = Flask(__name__)
store = TweetStore()
template = '..\FrontEnd\\index.html'

@app.route('/')
def index():
    tweets = store.tweets()
    return render_template(template, tweets = tweets)

if __name__ == '__main__':
    app.run(debug=True)