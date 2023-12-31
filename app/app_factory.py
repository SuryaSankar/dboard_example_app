from flask import Flask
from dboard import DboardFlask
from .views import pages_bp, api_bp
import json

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('app.default_config')
    app.config.from_pyfile('application.cfg.py')
    with open("app/menu.json") as f:
        nav_menu_items = json.load(f)
    DboardFlask(app, nav_menu_items=nav_menu_items)
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app