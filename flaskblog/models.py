from datetime import datetime, timedelta 
from flaskblog import db, login_manager

def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60),nullable = False)
    posts = db.Relationship('Post', backref = 'author', lazy = True)   
    #backref will give us chance to get row of the author when we call author of any post post.user (user equal to some row in this case which we get as user = User.query.first()), #lazy means data will be taken from database


    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow )
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False ) #table name is automatically set by model so it s lower case that is why we wrote user.id

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"