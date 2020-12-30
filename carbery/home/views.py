from flask import Blueprint
from flask import render_template


blueprint = Blueprint('home', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home/homepage.html')
