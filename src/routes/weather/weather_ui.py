from flask import Blueprint, render_template

bp = Blueprint('weather_ui', __name__, template_folder='templates')


@bp.get('/')
def handle_get_weather_info():
	return render_template('weather_ui.html')