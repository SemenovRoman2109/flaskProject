import flask 
from reg_app.models import User
from flask_login import login_user, current_user

def render_login():
    if flask.request.method == "POST":
        for user in User.query.filter_by(name = flask.request.form["name"]):
            if user.password == flask.request.form["password"]:
                login_user(user)
                return flask.redirect("/")
    
    is_admin = False
    if current_user.is_authenticated:
        is_admin = current_user.is_admin
    return flask.render_template("log.html", is_auth = current_user.is_authenticated, is_admin = is_admin)
