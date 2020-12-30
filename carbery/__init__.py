# Flask imports
from flask import Flask

# Etc
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Application imports
from carbery.settings import FLASK_APP_SETTINGS


# Define all managers
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.update(**FLASK_APP_SETTINGS)

    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from carbery.home.views import blueprint as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/', name='home')

    from carbery.users.views import blueprint as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user', name='user')

    from carbery.users.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=3000)
