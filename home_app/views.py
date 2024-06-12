import flask 
from shop_app.models import Product
from project.settings import DATABASE
from flask_login import current_user

def render_home():
    if flask.request.method == "POST":
        product = Product(
            name = flask.request.form["name"],
            description = flask.request.form["description"],
            count = flask.request.form["count"],
            price = flask.request.form["price"],
            discount = flask.request.form["discount"]
        )
        DATABASE.session.add(product)
        DATABASE.session.commit()

    is_admin = False
    if current_user.is_authenticated:
        is_admin = current_user.is_admin
    return flask.render_template(template_name_or_list= "home.html", is_admin = is_admin)