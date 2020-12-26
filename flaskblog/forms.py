from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

# Register Form
class RegistrationForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', 
        validators=[DataRequired(), Email()])

    password = PasswordField('Password', 
        validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', 
        validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        # Check if user exist
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already taken!')

    def validate_email(self, email):
        # Check if email exist
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already taken!')

# Login Form
class LoginForm(FlaskForm):
    email = StringField('Email', 
        validators=[DataRequired(), Email()])

    password = PasswordField('Password', 
        validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

# Update form
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', 
        validators=[DataRequired(), Email()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            # Check if user exist
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username already taken!')

    def validate_email(self, email):
        if email.data != current_user.email:
            # Check if email exist
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email already taken!')

# Post form
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

# Reset Form
class RequestResetForm(FlaskForm):
    email = StringField('Email', 
        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        # Check if email exist
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('That email does not exist! You must register first.')
# Reset Password
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', 
        validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', 
        validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Reset Password')