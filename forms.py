from flask_wtf import FlaskForm
from wtforms import *
#       from wtforms_components import ColorField
from wtforms.validators import Length, DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[Length(min=4,max=24),DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email(), Length(min=4,max=50)])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4,max=60)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),Length(min=4,max=60),EqualTo('password')])
    submit = SubmitField('Sign up')
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Length(min=4,max=24),DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4,max=60)])
    email = StringField('Email', validators=[DataRequired(),Email(), Length(min=4,max=50)])
    remeber = BooleanField('Remeber Me')
    submit = SubmitField('Login')
class ScheduleMakerForm(FlaskForm):
    className = StringField('class',validators=[DataRequired()])
    teacherName = StringField('teacher',validators=[DataRequired()])
    period = IntegerField('period',validators=[DataRequired()])
    weekday = StringField('dayOfTheWeek',validators=[DataRequired()])
    #colorCode = ColorField('colorCode',validators=[DataRequired()])
    time = TimeField('time',validators=[DataRequired()])
    duration = IntegerField('duration',validators=[DataRequired()])

    submit = SubmitField('Add Class')
