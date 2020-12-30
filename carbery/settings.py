# Clunky settings
import os


# Base settings
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Flask settings (flask, sql, etc.)
FLASK_APP_SETTINGS = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///carbery.db',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SECRET_KEY': os.urandom(32),
    'UPLOAD_FOLDER': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads'),
}
