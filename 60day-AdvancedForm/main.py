from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length
from wtforms.fields import EmailField

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators = [DataRequired(), Email()])
    password = PasswordField(label='Password', validators = [Length(min=3, max=20), DataRequired()])
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def submit():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)
        if login_form.email.data == "admin@email.com":
            if login_form.password.data == "12345678":
                return render_template('success.html', form=login_form)
            else:
                return render_template('denied.html', form=login_form)
        else:
            return render_template('denied.html', form=login_form)
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)