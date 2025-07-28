from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
	return render_template("index.html")

@bp.route('/pricing')
def pricing():
	return "Pricing"

@bp.route('/about')
def about():
	return "About"