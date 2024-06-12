import flask

app_reg = flask.Blueprint(
    name = "registration",
    import_name= "reg_app",
    template_folder= "templates"
)