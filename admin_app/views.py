import flask, os
from shop_app.models import Product
from project.settings import DATABASE
from flask_login import current_user

def render_admin():
    if flask.request.method == "POST":
        if "count" in flask.request.form:
            product = Product(
                name = flask.request.form["name"],
                description = flask.request.form["description"],
                price = flask.request.form["price"],
                count = flask.request.form["count"],
                discount = flask.request.form["discount"]
            )
            DATABASE.session.add(product)
            DATABASE.session.commit()
            uploaded_file = flask.request.files["image"]
            uploaded_file.save(os.path.abspath(__file__ + f"/../static/img/{product.name}.png"))
        else:
            product_id = int(flask.request.form["id"])
            product = Product.query.get(product_id)
            if flask.request.files["image"]:
                uploaded_file = flask.request.files["image"]
                uploaded_file.save(os.path.abspath(__file__ + f"/../static/img/{product.name}.png"))
            else:
                if flask.request.form["name"] == "":
                    DATABASE.session.delete(product)
                    DATABASE.session.commit()
                else:
                    new_name = flask.request.form["name"]
                    old_path = os.path.abspath(__file__ + f"/../static/img/{product.name}.png")
                    new_path = os.path.abspath(__file__ + f"/../static/img/{new_name}.png")
                    os.rename(old_path, new_path)
                    product.name = new_name
                    DATABASE.session.commit()
    if current_user.is_authenticated and current_user.is_admin:    
        return flask.render_template(template_name_or_list = 'admin.html', list_product = Product.query.all(), is_admin = current_user.is_admin)
    else:
        return flask.redirect("/")