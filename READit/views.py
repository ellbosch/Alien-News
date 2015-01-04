from READit import app
from flask import render_template, request, jsonify, redirect, current_app
from functools import wraps
import reddit
import json

# global array for all posts
POSTS_BUFFER = []

# class that holds buffer of reddit posts
class All_Posts():
    def __init__(self, sub, limit):
        self.posts = reddit.get_reddit_posts(sub, limit)
        self.index = 0

    def __iter__(self):
        return self

    def next(self):
        try:
            post = self.posts[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return post


def get_next_posts():
    posts = []
    for i in range(10):
        posts.append(POSTS_BUFFER.next())
    return posts



def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f(*args,**kwargs).data) + ')'
            return current_app.response_class(content, mimetype='application/javascript')
        else:
            return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def homepage():
    global POSTS_BUFFER
    sub = 'worldnews+science+tech+news'
    POSTS_BUFFER = All_Posts(sub, 100)
    posts = get_next_posts();    

    posts[0].isActive = True
    article = reddit.ArticlePost(posts[0].url)

    return render_template('index.html', post_list=posts, article=article) 


@app.route('/article/', methods=['GET'])
@support_jsonp
def show_article():
    url = str(request.args['url'])
    article = reddit.ArticlePost(url)

    return jsonify(result = {"title": article.title,
                             "text": article.text,
                             "url": article.url,
                             "summary": article.summary})


@app.route('/load-more/', methods=['GET'])
@support_jsonp
def load_more_articles():
    stop_iteration_hit = False
    posts = []

    try:
        posts = get_next_posts()
    except StopIteration:
        stop_iteration_hit = True
        
    return jsonify(result = {"posts": [p.serialize for p in posts],
                             "error": stop_iteration_hit})

