from RedditReader import app
from flask import render_template, request, jsonify
import reddit

# JSONP support
import json
from functools import wraps
from flask import redirect, current_app

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
    sub = 'worldnews+science+technology+news'
    posts = reddit.get_reddit_posts(sub, 10)
    posts[0].isActive = True

    article = reddit.ArticlePost(posts[0].url)

    return render_template('index.html', post_list=posts, article=article) 


@app.route('/article/', methods=['GET'])
@support_jsonp
def show_article():
    url = str(request.args['url'])
    article = reddit.ArticlePost(url)

    print "BAM:" + article.text

    return jsonify(result = {"title": article.title,
                             "text": article.text,
                             "image": article.image,
                             "url": article.url,
                             "summary": article.summary})
