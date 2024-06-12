from .settings import project
from cart_app import cart_app, render_cart
from home_app import home_app, render_home
from shop_app import shop, render_shop
from admin_app import admin_app, render_admin
from reg_app import app_reg, render_registration
from log_app import app_log, render_login

cart_app.add_url_rule(rule= "/cart/", view_func= render_cart, methods= ["GET","POST"])
home_app.add_url_rule(rule= "/", view_func= render_home, methods= ["GET","POST"])
shop.add_url_rule(rule= '/shop/', view_func= render_shop, methods= ["GET","POST"])
admin_app.add_url_rule(rule= '/admin/', view_func= render_admin, methods= ["GET","POST"])
app_log.add_url_rule(rule= '/login/', view_func= render_login, methods= ["GET","POST"])
app_reg.add_url_rule(rule= '/registration/', view_func= render_registration, methods= ["GET","POST"])

project.register_blueprint(blueprint= admin_app)
project.register_blueprint(blueprint= cart_app)
project.register_blueprint(blueprint= home_app)
project.register_blueprint(blueprint= app_reg)
project.register_blueprint(blueprint= app_log)
project.register_blueprint(blueprint= shop)