import flask

home_app = flask.Blueprint(
    name = "home",
    import_name= "home_app",
    template_folder= "templates"
)