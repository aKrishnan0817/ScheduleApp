from flask import Flask, render_template, url_for, flash, redirect
from dictionary import *
import helper
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY']='9d98a6c4fce07e21bcd58d3510ed23db'

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
