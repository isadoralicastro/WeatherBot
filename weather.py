from ctypes import windll
import requests
import json
from webex_bot.models.command import Command

class WeatherByZip(Command):
    def __init__(self):
        super().__init__(
            command_keyword="weather",
            help_message="Mostra o clima atual de acordo com o CEP digitado",
            card=None,
        )

    def execute(self, message, attachment_actions, activity):
        OPENWEATHER_KEY = "token da api"

        zip_code = message.strip()

        url = "https://api.openweathermap.org/data/2.5/weather?q=São%20Paulo,"
        url += f"zip={zip_code},{'BR'}&units=metric&appid={OPENWEATHER_KEY}&lang=pt_br"
        

        response = requests.get(url)
        weather = response.json()

        #  retorno da mensagem
        city = weather['name']
        conditions = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']

        response_message = f"Em {city}, a temperatura é de {temperature:.0f}°C com {conditions}. "
        response_message += f"A velocidade do vento é de {wind}mph. A humidade é de {humidity}% "

        return response_message