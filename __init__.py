import os
from flask import Flask, render_template

def create_app():
	#Initialize Flask App
	app = Flask(__name__)

	with app.app_context():
		from . import routes

	app.register_blueprint(routes.bp)
	
	return app