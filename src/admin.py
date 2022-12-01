import os
from flask_admin import Admin
from models import db, Controller, User, Entries
from flask_admin.contrib.sqla import ModelView


def setup_admin(app):
    app.secret_key = os.environ.get("FLASK_APP_KEY", "sample key")
    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
    admin = Admin(app, name="Smart Home", template_mode="bootstrap3")

    admin.add_view(ModelView(Controller, db.session))
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Entries, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))
