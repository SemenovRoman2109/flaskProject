import flask
from shop_app.models import Product
from flask_login import current_user

def render_cart():
    is_admin = False
    if current_user.is_authenticated:
        is_admin = current_user.is_admin
    if flask.request.cookies:
        products = flask.request.cookies.get('products').split(' ')
        # Зберігаємо всі продукти які отримаємо із моделі Product за id product який отримали з файлу cookies з назвою products
        list_products = []
        # Зберігаємо id продуктів що повторються в списку products лише в одному екземплярі
        repeate_id = []

        for id_product in products:
            count_products = products.count(id_product)
            if id_product not in repeate_id:
                list_products.append(Product.query.get(id_product))
                list_products[-1].count = count_products
                repeate_id.append(id_product)
                
        return flask.render_template(template_name_or_list = 'cart.html', products = list_products, is_admin = is_admin)
    else:
        return flask.render_template(template_name_or_list = 'cart.html', is_admin = is_admin)