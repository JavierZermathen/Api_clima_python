from consumo_api import get_weather_city


class Clima(object):

    def __init__ (self,main,visibility,wind,clouds):
        self.main = main
