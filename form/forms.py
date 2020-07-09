from wtforms import Form, SelectField, PasswordField, BooleanField, SubmitField,StringField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8,128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

class RichTextForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1,50)])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Publish')



if __name__ == '__main__':
    x = LoginForm()
    print(x.password)
    y = x.password.label
    print(y.__html__())