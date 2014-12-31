from RedditReader import app
from flask import render_template, request, jsonify
import reddit


@app.route('/')
def homepage():
    sub = 'worldnews+science+technology+news'
    posts = reddit.get_reddit_posts(sub, 10)
    posts[0].isActive = True

    article = reddit.ArticlePost(posts[0].url)

    return render_template('index.html', post_list=posts, article=article) 


@app.route('/article/')
def show_article():
    url = str(request.args['url'])
    article = reddit.ArticlePost(url)

    return jsonify(result = {"title": article.title,
                             "text": article.text,
                             "image": article.image,
                             "url": article.url,
                             "summary": article.summary})
