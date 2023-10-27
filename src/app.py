from flask import Flask


def create_app():
	app = Flask(__name__)

	from src.routes.weather import weather_ui, weather_api
	app.register_blueprint(weather_ui)
	app.register_blueprint(weather_api, url_prefix='/weather')
	app.config['REDIS_URL'] = "redis://:@redis_db:6379"

	from src.ext.redis import redis_client
	redis_client.init_app(app)

	return app
