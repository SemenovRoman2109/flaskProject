import flask

app_log = flask.Blueprint(
    name = "authorization",
    import_name= "log_app",
    template_folder= "templates"
)