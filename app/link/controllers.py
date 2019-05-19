import string
from random import choice

from flask import Blueprint, render_template, request, redirect, current_app, jsonify
from flask_login import current_user, login_required

from app.models import db, Link
from .forms import LinkForm


module = Blueprint('link', __name__)


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)


def make_page():
    alphabet = string.ascii_letters + string.digits
    page = ''.join(choice(alphabet) for i in range(8))
    return page


@module.route('/', methods=['GET'])
def index():
    form = LinkForm()
    return render_template('index.html', form=form)


@module.route('/process', methods=['POST'])
def process():
    form = LinkForm(request.form)
    if form.validate():
        page = make_page()
        short_link = request.host_url + page
        link = Link(page=page, short_link=short_link, **form.data)
        if current_user.is_authenticated:
            link.user = current_user
        db.session.add(link)
        db.session.commit()
        return jsonify({'short_link': short_link})
    return jsonify({'errors': form.full_link.errors[-1]})


# @module.route('/<page>')
# def _redirect(page):
#     link = Link.query.filter_by(page=page).first()
#     link.visits += 1
#     db.session.commit()
#     return redirect(f'{link.full_link}')


@module.route('/links', methods=['GET'])
@login_required
def link_list():
    links = Link.query.filter_by(user=current_user).order_by(Link.created.desc())
    return render_template('links.html', links=links)
