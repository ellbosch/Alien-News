from newspaper import Article
from flask import Flask, render_template, request, jsonify
import praw


app = Flask(__name__)


class RedditPost():
    def __init__(self, post):
        self.reddit_title = post.title
        self.url = post.url
        self.isActive = False


class ArticlePost():
    def __init__(self, url):
        article = Article(url=url)
        article.download()
        article.parse()

        self.title = article.title
        self.image = article.top_image
        self.text = article.text
        # self.summary = article.summary


def get_useragent():
    return praw.Reddit(user_agent='Alien News/1.0 by ellbosch')


def get_reddit_posts(subreddit, n):
    subreddit_posts = get_useragent().get_subreddit(subreddit).get_hot(limit=n)
    posts = []
    for p in subreddit_posts:
        post = RedditPost(p)
        posts.append(post)

    return posts


@app.route('/')
def homepage():
    sub = 'worldnews+science+technology'
    posts = get_reddit_posts(sub, 20)
    posts[0].isActive = True

    article = ArticlePost(posts[0].url)

    return render_template('index.html', post_list=posts, article=article) 


@app.route('/article/')
def show_article():
    url = str(request.args['url'])

    article = ArticlePost(url)

    return jsonify(result = {"title": article.title,
                             "text": article.text})


if __name__ == '__main__':
    app.run(debug=True)
