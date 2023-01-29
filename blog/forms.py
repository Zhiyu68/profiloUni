from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length, Regexp
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(),
                                    Email(message="The email address should be looked like 'example@example.com'.",granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    password = PasswordField(label="Password",
                             validators=[
                                 DataRequired(message='Password cannot be empty.'),
                                 Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",
                                     message='Minimum 8 characters, at least one uppercase letter, one lowercase letter and one number.')])
    name = StringField(label="Name",
                       validators=[
                           DataRequired(message='Username cannot be empty.'),
                           Length(min=6, max=18, message='Username length must be greater than 6 and less than 18.')])
    submit = SubmitField("Sign Me Up!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign in!")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")