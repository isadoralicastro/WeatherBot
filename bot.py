from webex_bot.webex_bot import WebexBot 
import os 
from webex_bot.commands.echo import EchoCommand
from weather import WeatherByZip

webex_token = os.getenv('WEBEX_TOKEN')

bot = WebexBot(webex_token , approved_domains=["cesconbarrieu.com.br"])

# Add new commands for the bot to listen out for.
bot.add_command(EchoCommand())
bot.add_command(WeatherByZip())

bot.run()

