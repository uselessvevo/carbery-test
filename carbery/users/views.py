import os
import hashlib

# Flask imports
import string
import random

from flask import Blueprint, flash
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for

# Flask login
from flask_login import login_user
from flask_login import current_user
from flask_login import login_required

# Package imports
from carbery import db
from carbery.settings import FLASK_APP_SETTINGS
from carbery.users.forms import LoginForm, RegistrationForm
from carbery.users.models import User, Image


blueprint = Blueprint(name='user', import_name=__name__)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """ Register a new user """
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            password=form.password.data,
            is_active=True
        )
        login_user(new_user, True)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home.home'))
    return render_template('users/register.html', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """ Log in an existing user """
    form = LoginForm()
    if form.validate_on_submit():
        # Get user
        user = db.session.query(User).filter(
            User.username == form.username.data
        ).first()

        if user:
            login_user(user, True)
            return render_template('home/homepage.html', form=form)
        else:
            flash('Incorrect username or password')

    return render_template('users/login.html', form=form)


@blueprint.route('/upload-file', methods=['GET', 'POST'])
@login_required
def upload_file():
    """ Upload image. No error handlers, checks """
    if request.method == 'POST':
        # response = Response()
        # response.headers['X-Auth-User'] = current_user.id

        file = request.files['file1']
        new_filename = ''.join(random.choice(string.ascii_letters) for _ in range(50))
        new_filename = '%s_%s' % (file.filename, new_filename)

        user = db.session.query(User).filter(
            User.username == current_user.username
        ).first()

        # No unique images and hashes checks
        file_hash = file.read()
        file.save(os.path.join(FLASK_APP_SETTINGS['UPLOAD_FOLDER'], file.filename))

        new_image = Image(
            filename=new_filename,
            hash_md5=hashlib.md5(file_hash).hexdigest(),
            hash_sha256=hashlib.sha256(file_hash).hexdigest(),
            user_id=user.id
        )

        db.session.add(new_image)
        db.session.commit()

        return redirect(url_for('home.home')), 200, [('X-Auth-User', current_user.id)]

    return render_template('users/upload-file.html')
