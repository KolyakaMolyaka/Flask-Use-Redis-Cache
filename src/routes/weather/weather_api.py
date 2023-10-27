from http import HTTPStatus
from flask import Blueprint, jsonify, request, render_template
from src.core.weather import process_get_weather_request

bp = Blueprint('weather_api', __name__, template_folder='templates')


@bp.post('/')
def get_weather_from_form():
	city = request.form.get('city').strip()
	weather = process_get_weather_request(city)
	return render_template('weather_ui.html', city=city, weather=weather)


@bp.get('/<string:city>')
def get_weather(city):
	weather = process_get_weather_request(city)
	response = jsonify({
		'weather': weather
	})
	response.status_code = HTTPStatus.OK
	return response
