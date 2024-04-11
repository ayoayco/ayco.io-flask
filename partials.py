from flask import Blueprint, render_template, send_from_directory
from jinja2 import TemplateNotFound
from datetime import datetime

partials = Blueprint('partials', __name__, template_folder='partials')

@partials.route('/', defaults={'page': 'index'})
@partials.route('/<page>')
def show(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        return send_from_directory('dist', '404.html'), 404

@partials.route('feed')
def feed():
    return render_template(f'feed.html', date=datetime.now().strftime('%B %d, %Y, %H:%M:%S'))
