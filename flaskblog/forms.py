from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(),Length(min=2,max=20)]
                            )
    email = StringField('Email',
                        validators=[DataRequired(), Email()]
                        )
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                        validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):

        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That username is taken, Please choose a different one') 
    
    
    def validate_email(self,email):

        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('That email is used, Please choose a different one')




class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()]
                        )
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


#for creating db in terminal run:
#python
#from flaskblog(py file name) import app, db
#app.app_context().PUSH()  need to add push to the end
#db.create_all()

#dp.drop_all() #DO NOT USE: it is for deleting all tables and data inside it

#FOR ADDING DATA to SQLite from terminal
#from flaskblog (filename) import User, Post (CLASSES
#user_1 = User(username = 'shah',email='c@demo.com', password = 'password')
#db.session_add(user_1)                                       WINDOWS: db.session.add(user_1)
#db.commit ()   #after this data will be recorded to the DB   WINDOWS: db.session().commit() 
#
#User.query.all(), User.query.filter_by(username = 'shah').first() /all() (as list)  to get data
