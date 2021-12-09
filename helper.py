from flask import render_template

def valid_login(username, password):
    if(username=="pikachu" and password=="eclair"):
        return True
    else:
        return False

def log_the_user_in(username):
    return render_template('hello.html', name=username)