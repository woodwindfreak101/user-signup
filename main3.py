from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def display_user_signup():
    return render_template('signup_form.html')
#.format(username='',username_error='',user_password='',user_password_error='',verify_user_password='',
#verify_password_error='',user_email='',user_email_error='')

def correct_length(text):
    if len(text) > 3 and len(text) <= 20 and " " not in text:
        return True
    else:
        return False

def passwords_match(text, text2):
    if text == text2:
        return True
    else:
        return False

def proper_email(email):
    if "." in email and "@" in email:
        if correct_length(email):
            return True
        else: 
            return False
    else:
        return False 

@app.route('/', methods=['POST'])
def validate_user():

    username = request.form['username']
    user_password = request.form['user_password']
    verify_user_password = request.form['verify_user_password']
    user_email = request.form['user_email']

    user_password_error = ''
    username_error = ''

    if not correct_length(username):
        username_error = "Username must be between 4 and 20 characters long, and cannot have spaces."
        username=''
        return render_template('signup_form.html',username_error=username_error,username=username)

    if not correct_length(user_password):
        user_password_error = "Your password must be between 4 and 20 characters long, and cannot contain spaces."
        user_password=''
        return render_template('signup_form.html',user_password_error=user_password_error,user_password=user_password,user_email=user_email,username=username)

    if not passwords_match(user_password, verify_user_password):
        user_password_error = "Your passwords must match exactly, be between 4 and 20 characters long, and cannot have spaces."
        user_password=''
        verify_user_password=''
        return render_template('signup_form.html',user_password_error=user_password_error,user_password=user_password,verify_user_password=verify_user_password,user_email=user_email,username=username)

    if not user_email == '':
        if not proper_email(user_email):
            user_email_error = "please have between 4 and 20 characters in your email, one period and one @ in your email."
            user_email=''
            return render_template('signup_form.html',user_email_error=user_email_error,user_email=user_email)
        else: 
            return render_template('welcome_username.html',username=username)
                #'signup_form.html',username=username,username_error=username_error,password='',
                #user_password_error=user_password_error,verify_password='',user_email='',user_email_error='')
    else:
        return render_template('welcome_username.html',username=username)

#    else:
#        return "<h1>Success</h1>"
#        return signup_form.format(username=username,username_error=username_error,password='',user_password_error='',verify_password='',
#        verify_password_error='',user_email_error='')



app.run()