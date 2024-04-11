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

@partials.route('example')
def example():
    return render_template(f'example.html', date=datetime.now().strftime('%B %d, %Y'))
