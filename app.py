from flask import Flask, render_template, url_for, flash, redirect
from dictionary import *
import helper
from forms import *
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY']='9d98a6c4fce07e21bcd58d3510ed23db'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///schedule.db'

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    email = db.Column(db.String(50),unique=True, nullable=False)
    image_file = db.Column(db.String(40),nullable=False, default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    schedule = db.relationship('Schedule',backref='username')
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

@app.route('/',methods=['GET',"POST"])
def index():
    return render_template('home.html')
@app.route('/schMaker')
def schMaker():
    form = ScheduleMakerForm()
    return render_template('schMaker.html',form=form,title="Schedule Maker")
@app.route('/schedule')
def schedule():
    timeData = helper.time()
    return render_template('time.html',posts=posts,time=timeData)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "bob@bob.com" and form.username.data=="bobster88" and form.password.data == "bob123":
            flash('Successful Login','success')
            return redirect(url_for('index'))
        else:
            flash('Login Failed','danger')
    return render_template('login.html',form=form,title="Login")
