from weather_data.data import get_temperature, get_humidity


def is_weather_comfortable():
    temp = get_temperature()
    hum = get_humidity()

    # Условие комфортности: комфортно, если температура от 18 до 25 градусов и влажность ниже 80%
    if temp is not None and hum is not None:
        return 18 <= temp <= 25 and hum < 80
    return False
