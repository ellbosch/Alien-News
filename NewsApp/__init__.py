from flask import Flask
 
app = Flask(__name__)
 
app.secret_key = 'development key'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cheese1223@localhost/development'

from models import db
db.init_app(app)

import NewsApp.routes
