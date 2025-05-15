# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

# 로그인 폼
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# 회원가입 폼
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# 설문조사 폼
class SurveyForm(FlaskForm):
    question1 = StringField('Question 1', validators=[DataRequired()])
    question2 = StringField('Question 2', validators=[DataRequired()])
    question3 = StringField('Question 3', validators=[DataRequired()])
    submit = SubmitField('Submit Survey')
