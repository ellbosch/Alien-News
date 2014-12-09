from flask import Flask
from flask import request
from flask import render_template
from newspaper import Article
import praw


app = Flask(__name__)


class RedditPost():
    def __init__(self, post):
        self.reddit_title = post.title

        # use newspaper module to download article information
        article = Article(url=post.url)
        article.download()
        article.parse()

        self.article_title = article.title
        self.image = article.top_image



def get_useragent():
    return praw.Reddit(user_agent='Alien News/1.0 by ellbosch')


@app.route('/')
def homepage():
    world_news_posts = get_useragent().get_subreddit('worldnews').get_hot(limit=2)

    posts = []
    for p in world_news_posts:
        post = RedditPost(p)
        posts.append(post)


    return render_template('index.html', post_list=posts)


if __name__ == '__main__':
    app.run(debug=True)