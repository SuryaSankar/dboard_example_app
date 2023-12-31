from werkzeug.serving import run_simple
from app import app_factory


application = app_factory.create_app()


if __name__ == "__main__":
    application.run(
        use_debugger=True, debug=True, 
        use_reloader=True, host="0.0.0.0")