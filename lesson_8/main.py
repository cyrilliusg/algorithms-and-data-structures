from weather_data.data import set_weather
from weather_analysis.analysis import is_weather_comfortable

# Установка погодных данных
set_weather(22, 70)  # 22 градуса и 70% влажности

# Проверка комфортности погоды
print(is_weather_comfortable())  # Должно вернуть True, если погода комфортна

