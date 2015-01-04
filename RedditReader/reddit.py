import nltk
nltk.data.path.append('./nltk_data/')
from newspaper import Article, Config
import praw
import lxml.html.clean
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class RedditPost():
    def __init__(self, post):
        self.reddit_title = post.title
        self.url = post.url
        self.subreddit = str(post.subreddit)
        self.isActive = False

    @property
    def serialize(self):
        return {
            'reddit_title': self.reddit_title,
            'url': self.url,
            'subreddit': self.subreddit,
            'isActive': self.isActive
        }


class ArticlePost():
    def __init__(self, url):
        c = Config()
        c.keep_article_html = True

        article = Article(url=url, config=c)
        article.download()
        article.parse()
        
        try:
            article.nlp()
            summary = article.summary
            if summary == "":
                self.summary = "Summary not available!"
            else:
                self.summary = summary
        except Exception, e:
            self.summary = "Summary not available!"

        self.title = article.title
        self.text = article.article_html
        self.url = url
        # self.image = article.top_image


def get_useragent():
    return praw.Reddit(user_agent='Reddit Reader/1.0 by /u/ellbosch')


def get_reddit_posts(subreddit, n):
    subreddit_posts = get_useragent().get_subreddit(subreddit).get_hot(limit=n)
    posts = []
    for p in subreddit_posts:
        post = RedditPost(p)
        posts.append(post)

    return posts
