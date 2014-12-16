from NewsApp import app
from newspaper import Article
import praw
from flask import render_template, request, flash, session, url_for, redirect
from forms import SignupForm, SigninForm
from models import db, User
import time
 
app.secret_key = 'development key'

class RedditPost():
    def __init__(self, post):
        self.reddit_title = post.title

        # use newspaper module to download article information
        article = Article(url=post.url)
        article.download()
        article.parse()

        self.article_title = article.title
        self.image = article.top_image

def timerDecorator(f):
  def new_f(*args):
    t1 = time.clock()
    result = f(*args)
    t2 = time.clock()
    t_elapsed = t2 - t1
    print "Elapsed Time: " + str(t_elapsed)

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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  
  if 'email' in session:
    return redirect(url_for('profile'))

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      session['email'] = newuser.email
      return redirect(url_for('profile'))
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)

@app.route('/profile')
def profile():
  if 'email' not in session:
    return redirect(url_for('signin'))
    
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
  
  if 'email' in session:
    return redirect(url_for('profile'))

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('homepage'))

@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'
# if __name__ == '__main__':
#   app.run(debug=True)