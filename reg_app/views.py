import flask 
from .models import User
from project.settings import DATABASE
from flask_login import current_user

def render_registration():
    if flask.request.method == "POST":
        user = User(
            name = flask.request.form["name"], 
            password = flask.request.form["password"],
            is_admin = False
        )
        try: 
            DATABASE.session.add(user)
            DATABASE.session.commit()
            return flask.redirect("/login/")
        except:
            return "Не вдалось створити користува"
        
    is_admin = False
    if current_user.is_authenticated:
        is_admin = current_user.is_admin
    return flask.render_template("reg.html", is_auth = current_user.is_authenticated, is_admin = is_admin)

