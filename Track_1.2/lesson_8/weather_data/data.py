temperature = None
humidity = None


def set_weather(temp, hum):
    global temperature, humidity
    temperature = temp
    humidity = hum


def get_temperature():
    return temperature


def get_humidity():
    return humidity
