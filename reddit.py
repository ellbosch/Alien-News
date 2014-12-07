from flask import Flask
from flask import request
import praw


app = Flask(__name__)


def get_useragent():
    return praw.Reddit(user_agent='Alien News/1.0 by ellbosch')


@app.route('/')
def homepage():
    news = get_useragent().get_subreddit('worldnews').get_hot(limit=5)
    return str([str(x) for x in news])


if __name__ == '__main__':
    app.run(debug=True)