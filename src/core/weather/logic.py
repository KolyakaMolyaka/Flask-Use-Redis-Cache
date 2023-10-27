from functools import wraps

from src.ext.redis import redis_client


def cache_weather(cache_time: int = 60):
	def wrapper(func):
		@wraps(func)
		def decorator(city: str):
			weather = redis_client.get(city)
			if not weather:
				weather = func(city)
				redis_client.set(city, weather, ex=cache_time)
				return weather
			else:
				return weather.decode('utf-8') + ' (cached)'

		return decorator

	return wrapper


@cache_weather(cache_time=5)
def process_get_weather_request(city: str):
	city_to_weather = {
		'Lipetsk': 'Snowy',
		'Kaliningrad': 'Rainy',
		'Moscow': 'Windy'
	}
	return city_to_weather.get(city, 'City unknown.')
